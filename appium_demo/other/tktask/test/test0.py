import json
import random
import time

from selenium import webdriver
import requests

headers = {"Accept": "application/json",
           'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           'Cookie': '_ga=GA1.2.221321654.1571713017; _gid=GA1.2.1458812847.1571713017; tt_webid=6750458410351052291',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           "X-Requested-With": "XMLHttpRequest",
           }


class SeleniumClient:
    target_url = 'https://www.iesdouyin.com/share/video/6750200599184297228/?region=CN&mid=6750187224442096398&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme'  # 分享链接

    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.proxy_meta = ''
        self.agent = headers["User-Agent"]
        # self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('lang=zh_CN.UTF-8')
        self.chromeOptions.add_argument('user-agent="%s"' % self.agent)
        self.browser = webdriver.Chrome(options=self.chromeOptions)

    def test_js(self):
        self.browser.get("https://www.baidu.com/")
        # 给搜索输入框标红javascript脚本
        js = "var q=document.getElementById(\"index-bn\");q.style.border=\"2px solid red\";"
        # 调用给搜索输入框标红js脚本
        self.browser.execute_script(js)
        time.sleep(3)
        # 单独执行js脚本
        self.browser.execute_script('alert("输入框标红了!")')
        time.sleep(3)

    def go_url(self):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            self.browser.get(self.target_url)
            # self.browser.execute_script('alert("输入框标红了!")')
            # time.sleep(3)
            # js = 'var sign=_bytedAcrawler.sign(\"104713356413\")'
            # time.sleep(100)
            # sign = self.browser.execute_script(js)
            video = self.browser.find_element_by_xpath('//*[@id="theVideo"]')
            src = video.get_attribute('src')
            print(src)
        except Exception as e:
            print(e)
        finally:
            self.quit()

    def quit(self):
        if self.browser: self.browser.quit()


def signature():
    seleniumclient = SeleniumClient()
    seleniumclient.go_url()

    # sign = seleniumclient.go_url()
    # print("sign=" + sign)

    # https://www.iesdouyin.com/share/user/110677980134
    # (function() {
    # $(function(){
    #     __M.require(‘douyin_falcon:page/reflow_user/index’).init({
    #     uid: “110677980134”,
    # dytk: ‘061ae6e81229e178146aa674327eba89’
    # });
    # });
    # })();


def get_user_video_list_by_uid(user_id, cursor=0):
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?'
    sign, dytk = signature(user_id)
    # pass
    sign = 'R2PPZRAeGs-vue0YFhi0nkdjz3'
    dytk = 'ac5e995179f3a8a16d1f5e7266ea6a08'
    print("sign:%s,dytk:%s" % (sign, dytk))
    if sign is None or dytk is None:
        print("sign [%s] or dytk [%s] is none" % (sign, dytk))
        return None
    params = {
        "user_id": user_id,
        "count": "21",
        "max_cursor": cursor,
        "aid": "1128",
        "_signature": sign,
        "dytk": dytk
    }
    res = requests.get(url, headers=headers, params=params)
    try:
        print.info("request url: %s" % res.url)
    except:
        pass
    content = res.content.decode("utf8")
    print("content" + content)
    jsn = json.loads(content)
    return jsn


if __name__ == '__main__':
    user_id = '104713356413'
    # get_user_video_list_by_uid(user_id)
    signature()
