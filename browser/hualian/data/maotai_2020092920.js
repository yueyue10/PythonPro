$(function () {
    const moutaiPromoDetailAPI = "https://maot.beijing-hualian.com/api/moutai/V1.0/promoDetail"
    const getCodeAPI = "https://maot.beijing-hualian.com/api/moutai/V2.0/getCode"
    const buyMoutaiAPI = "https://maot.beijing-hualian.com/api/moutai/V3.0/buy_moutai"

    // const moutaiPromoDetailAPI = "https://mingsitech.com/api/moutai/V1.0/promoDetail"
    // const getCodeAPI = "https://mingsitech.com/api/moutai/V2.0/getCode"
    // const buyMoutaiAPI = "https://mingsitech.com/api/moutai/V3.0/buy_moutai"

    var saleStartTime = ""
    var codeMethod_ = ""
    var showChannelList = []
    var channelList_ = []
    var promoPointType = ""
    var promoPointsList = []
    var promoPointsList_ = []
    var intervalTime = ""
    var timecount = 30
    var ipone = ""
    var cilckFn = true
    var codeNo = ""
    var slide_code = false
    var addInfo = false
    var canBuyNum = ""
    var takeEndTime_ = ""
    var takeStartTime_ = ""
    var timeList_ = []
    var timeListName = []
    var isRemainPoint_ = false

    moutaiPromoDetail()
    function moutaiPromoDetail() {
        maotaiTime()
        let params = {
            token: GetQueryString("token"),
            channelId: GetQueryString("channelId"),
            moutaiPromoId: GetQueryString("moutaiPromoId"),
        }
        $.ajax({
            type: "GET",
            url: moutaiPromoDetailAPI,
            data: encryption(params),
            success(res) {
                let data = decryption(res)
                console.log('data: ', data);
                let { canBuy, codeMethod, channelList, promo, name, idNo, takeStartTime, takeEndTime, timeList, reason, points } = data.data;
                clearInterval(intervalTime);
                if (promo.promoPointType == "L") {
                    data.data.promoPointsList.map((item, i) => {
                        if (points > item.points || points == item.points) {
                            isRemainPoint_ = true
                        }
                    });
                } else {
                    isRemainPoint_ = true
                }

                if (isRemainPoint_ && canBuy) {
                    if (promo.promoPointType === 'SP') {
                        $(".btn").text(`预约购买`).css({ "background": "#005a45" })
                        cilckFn = false
                    } else {
                        let isSaleTime = timeDifference(promo.saleStartTime, promo.saleEndTime, res.timestamp, promo.promoPointType)
                        if (isSaleTime == 3 && channelList.length > 0) {
                            $(".btn").text(`预约购买`).css({ "background": "#005a45" })
                            cilckFn = false
                        } else if (isSaleTime === 2 || channelList.length === 0) {
                            $(".btn").text(`明日${promo.saleStartTime.substring(11, 16)}开始预约`).css({ "background": "#8E8F91" })
                            cilckFn = true
                            return
                        } else if (isSaleTime === 1) {
                            $(".btn").text(`今日${promo.saleStartTime.substring(11, 16)}开始预约`).css({ "background": "#8E8F91" })
                            cilckFn = true
                            return
                        }

                    }
                }
                if (!canBuy) {
                    $(".btn").text(reason).css({ "background": "#8E8F91" })
                    cilckFn = true
                    return
                }

                if (!isRemainPoint_) {
                    $(".btn").text('您今日可抢购数量：0').css({ "background": "#8E8F91" })
                    cilckFn = true
                    return
                }


                // if (promo.canBuyNum == 0) {
                //     cilckFn = true
                //     $(".btn").text(`今日可购买数量：0`).css({ "background": "#8E8F91" })
                //     return
                // }

                $("#tip_").text(`1.取货日期起${promo.subscribeEffectDay == 0 ? '当' : promo.subscribeEffectDay + 1}日内有效，限本人领取，不可提前领取`)

                $(".btn").text(`预约抢购`).css({ "background": "#005a45" })
                cilckFn = false
                codeMethod_ = codeMethod

                if (!name) {
                    $("#name").val("请到个人中心完善信息")
                    addInfo = true
                } else {
                    $("#name").val(name)
                }

                if (!idNo) {
                    $("#idNo").val("请到个人中心完善信息")
                    addInfo = true
                } else {
                    $("#idNo").val(idNo)
                }

                if (!timeList) {
                    $("#timeList").hide()
                } else {
                    timeListName = timeList.map(i => (`${i.startTime.substring(11, 16)}至${i.endTime.substring(11, 16)}`))
                    timeList_ = timeList
                }

                idNo_ = idNo
                saleStartTime = `${promo.saleStartTime.substring(11, 13)} : ${promo.saleStartTime.substring(14, 16)}`;
                showChannelList = channelList.map(i => (i.channelName))
                channelList_ = channelList
                promoPointType = promo.promoPointType
                promoPointsList = promo.pointsList.map(i => (i.itemNum))
                promoPointsList_ = data.data.promoPointsList
                canBuyNum = promo.canBuyNum
                takeEndTime_ = takeEndTime.substring(0, 10)
                takeStartTime_ = takeStartTime.substring(0, 10)
            }
        })
    }

    function timeDifference(begin, end, data, promoPointType) {
        if (promoPointType === 'SP') {
            return 2
        }
        if (begin && end) {
            const beginHour = begin.substr(11, 2);
            const beginMin = begin.substr(14, 2);
            begin = new Date().setHours(beginHour, beginMin);
            const endHour = end.substr(11, 2);
            const endMin = end.substr(14, 2);
            end = new Date().setHours(endHour, endMin);

            if (data < begin) {
                return 1
            } else if (data > end) {
                return 2
            } else {
                return 3
            }
        }
    }


    $(".btn").click(function () {
        if (!cilckFn) {
            $("html").css({ "overflow": "hidden" })
            getCode()
            init()
        }
    })


    function maotaiTime() {
        intervalTime = setInterval(() => {
            timecount--;
            $(".btn").text("正在获取活动数据 " + timecount + "s").css({ "background": "#8E8F91" })
            if (timecount == -1) {
                clearInterval(intervalTime)
                timecount = 30
                $(".btn").text("当前抢购人数较多，请重试 ").css({ "background": "#8E8F91" })
                showMoudel()
            }
        }, 1000);
    }

    function showMoudel() {
        $.confirm({
            title: '提示',
            text: '当前抢购人数较多，请重试',
            onOK: function (username, password) {
                moutaiPromoDetail()
            },
            onCancel: function () {
                wx.miniProgram.navigateBack({ delta: 1 })
            },
            buttonOK: "重试",
            buttonCancel: "退出",

        });
    }

    function init() {
        $("#time").picker({
            title: "取货时间",
            cols: [
                {
                    textAlign: 'center',
                    values: getAllDate(takeStartTime_, takeEndTime_)
                }
            ]
        });

        $("#channel").picker({
            title: "预售门店",
            cols: [
                {
                    textAlign: 'center',
                    values: showChannelList
                }
            ]
        });

        $("#num").picker({
            title: "预约数量",
            cols: [
                {
                    textAlign: 'center',
                    values: promoPointsList
                }
            ],
            onChange(e) {
                let data = promoPointsList_.find(i => i.itemNum == e.value.join(""))
                debugger
                $("#payMode").val(`到店付款${data.sellPrice / 100}`)
                $("#points").val(`积分扣减${data.points}`)
            }
        });


        if (promoPointType == 'L') {
            $("#num_L").show()
            $("#payMode_").show()
        } else {
            $("#payMode").hide()
            $("#num_UL").show()
        }

        if (promoPointType == "L" && codeMethod_ == "IMAGE_CODE") {
            $("#code_UL").show()
        }

        if (promoPointType == "L" && codeMethod_ == "SLIDE_CODE") {
            slide_code = true
        }

        $("#timeListId").picker({
            title: "领取时间段",
            cols: [
                {
                    textAlign: 'center',
                    values: timeListName
                }
            ]
        });
    }



    function getCode() {
        if (promoPointType == "UL" || codeMethod_ == "IMAGE_CODE") {
            var isShow = true
            $.showLoading("正在加载...");
            setTimeout(function () {
                if (isShow) {
                    $.hideLoading();
                    $.alert("当前抢购人数较多，请重试", function () {
                        $.closeModal();
                    });
                }
            }, 10000)
            let params = {
                token: GetQueryString("token"),
                channelId: GetQueryString("channelId"),
                moutaiPromoId: GetQueryString("moutaiPromoId"),
            }
            $.ajax({
                type: "GET",
                url: getCodeAPI,
                data: encryption(params),
                success(res) {
                    $.hideLoading();
                    isShow = false
                    $("#code").attr('src', `data:image/png;base64,${res}`);
                    $("#code_UL").show()
                    $(".popup").show()
                }
            })
        } else {
            $(".popup").show()
        }
    }
    function arrayBufferToBase64(buffer) {
        var binary = '';
        var bytes = new Uint8Array(buffer);
        var len = bytes.byteLength;
        for (var i = 0; i < len; i++) {
            binary += String.fromCharCode(bytes[i]);
        }
        return window.btoa(binary);
    }

    $("#changeOne").click(function () {
        let params = {
            token: GetQueryString("token"),
            channelId: GetQueryString("channelId"),
            moutaiPromoId: GetQueryString("moutaiPromoId"),
        }
        $.ajax({
            type: "GET",
            url: getCodeAPI,
            data: encryption(params),
            success(res) {
                $("#code").attr('src', `data:image/png;base64,${res}`);
            }
        })
    })

    function goBuyMoutai() {
        $.showLoading("预购中...");
        let channelId = channelList_.find(i => i.channelName == $("#channel").val()).channelId
        let index = timeListName.indexOf($("#timeListId").val())
        if (index > -1) {
            var timeListId = timeList_[index].id
        }
        let params = {
            token: GetQueryString("token"),
            channelId: channelId,
            moutaiPromoId: GetQueryString("moutaiPromoId"),
            num: promoPointType == "UL" ? $("#num_ul").val() : $("#num").val(),
            subscribeTime: $("#time").val() + " 00:00:00",
            name: $("#name").val(),
            idNo: $("#idNo").val(),
            code: $("#codeNo").val() || codeNo,
            subscribeTimeId: index != -1 ? timeListId : '',
            phone: GetQueryString("phone"),
        }
        console.log('params', params);
        $.ajax({
            type: "POST",
            url: buyMoutaiAPI,
            data: encryption(params),
            success(res) {
                $.hideLoading();
                if (res.httpCode == 200) {
                    let orders = decryption(res).data
                    canBuyNum = orders.canBuyNum
                    wx.miniProgram.redirectTo({
                        url: `/pages/share/share?imgUrl=${orders.imgUrl}&tgManNum=${orders.tgManNum}&promoName=${orders.promoName}&storeName=${orders.storeName}&promoTitle=${orders.promoTitle}&remainPeople=${orders.remainPeople}&promoEndTime=${orders.promoEndTime}&promoType=preOrder&subscribeTime=${orders.subscribeTime}&navigationBarTitleText=预约成功`
                    })
                } else {
                    $.alert(res.msg);
                }
            },
            error(res) {
                $.hideLoading();
                $.alert(res.msg);
            }
        })

    }

    function encryption(params) {
        if (!params) return null
        let text = `wxmo12ui90ijWNST`
        let key = CryptoJS.enc.Utf8.parse(text);
        let iv = CryptoJS.enc.Utf8.parse('bWFsbHB3ZA==WNST');
        let ordered = {};
        let str = ''
        params.timestamp = new Date().getTime();
        Object.keys(params).sort().forEach(function (key) {
            ordered[key] = params[key];
            str += `${key}=${params[key]}&`
        });
        str += 'key=LeTou-2016MS';
        ordered.sign = CryptoJS.MD5(str).toString();
        let AesEncrypted = CryptoJS.AES.encrypt(JSON.stringify(ordered), key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return {
            formData: AesEncrypted.toString(),
        }
    }

    function decryption(body) {
        if (!body.data) return {}
        let key = CryptoJS.enc.Utf8.parse(`wxmo12ui90ijWNST`);
        let iv = CryptoJS.enc.Utf8.parse('bWFsbHB3ZA==WNST');
        let AesDecrypted = CryptoJS.AES.decrypt(body.data, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        let str = CryptoJS.enc.Utf8.stringify(AesDecrypted);
        try {
            body.data = JSON.parse(str);
        } catch (e) {
            body.data = str;
        }
        return body
    }

    function GetQueryString(name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
        var r = window.location.search.substr(1).match(reg); //获取url中"?"符后的字符串并正则匹配
        var context = "";
        if (r != null)
            context = r[2];
        reg = null;
        r = null;
        return context == null || context == "" || context == "undefined" ? "" : context;
    }

    var mySwiper = new Swiper('.swiper-container', { autoplay: true })
    var myCaptcha = _dx.Captcha(document.getElementById('captcha'), {
        appId: '61925e4f697671f9b492eee4bf9139ae',
        style: "oneclick",
        success: function (token) {
            codeNo = token
            myCaptcha.hide();
            goBuyMoutai()
            setTimeout(function () {
                myCaptcha.reload();
            }, 1000);

        },
        fail: function (error) {
            myCaptcha.reload();
        },

    });

    function format(time) {
        let ymd = ''
        let mouth = (time.getMonth() + 1) >= 10 ? (time.getMonth() + 1) : ('0' + (time.getMonth() + 1))
        let day = time.getDate() >= 10 ? time.getDate() : ('0' + time.getDate())
        ymd += time.getFullYear() + '-' // 获取年份。
        ymd += mouth + '-' // 获取月份。
        ymd += day // 获取日。
        return ymd // 返回日期。
    }

    function getAllDate(start, end) {
        let dateArr = []
        let startArr = start.split('-')
        let endArr = end.split('-')
        let db = new Date()
        db.setUTCFullYear(startArr[0], startArr[1] - 1, startArr[2])
        let de = new Date()
        de.setUTCFullYear(endArr[0], endArr[1] - 1, endArr[2])
        let unixDb = db.getTime()
        let unixDe = de.getTime()
        let stamp
        const oneDay = 24 * 60 * 60 * 1000;
        for (stamp = unixDb; stamp <= unixDe;) {
            dateArr.push(format(new Date(parseInt(stamp))))
            stamp = stamp + oneDay
        }
        return dateArr
    }



    function getNowFormatDate() {
        var date = new Date();
        var year = date.getFullYear();
        var month = date.getMonth() + 1;
        var strDate = date.getDate();
        if (month >= 1 && month <= 9) {
            month = "0" + month;
        }
        if (strDate >= 0 && strDate <= 9) {
            strDate = "0" + strDate;
        }

        return `${year}-${month}-${strDate} `;
    }

    $(".m_btn").click(function () {
        var channel = $("#channel").val()
        var num = $("#num").val()
        var time = $("#time").val()

        if (!channel) {
            $.alert("请选择门店");
            return
        }


        if (promoPointType == 'L') {
            if (!num) {
                $.alert("请选择数量");
                return
            }
        } else {
            if (!$("#num_ul").val()) {
                $.alert("请选择数量");
                return
            }
        }

        if (!time) {
            $.alert("请选择取货时间");
            return
        }
        if (addInfo) {
            $.alert("请到个人中心完善信息");
            return
        }


        if (canBuyNum == 0) {
            $.alert("已达到购买瓶数");
            return
        }

        if (slide_code) {
            myCaptcha.show();
        } else {
            if (!$("#codeNo").val()) {
                $.alert("请填写验证码");
                return
            }
            goBuyMoutai()
        }
    })

    $(".topTitle .showNotice").click(function () {
        wx.miniProgram.navigateTo({ url: '/packageA/moutai_notice/moutai_notice' })
    })

    $(".close").click(function () {
        $("html").css({ "overflow": "auto" })
        $(".popup").hide()
    })

    $(".reduce").click(function () {
        let num = $("#num_ul").val()
        if (num > 1) {
            $("#num_ul").val(num - 1)
        }
    })
    $(".add").click(function () {
        let num = $("#num_ul").val()
        if (num <= 100) {
            $("#num_ul").val(+num + 1)
        }
    })

})
