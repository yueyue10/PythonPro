import json

import requests


def get_video_detail_by_id(video_id):
    url = "https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?version_code=6.5.0&pass-region=1&pass-route=1&js_sdk_version=1.16.2.7&app_name=aweme&vid=9D5F078E-A1A9-4F64-81C7-F89CA6A3B1DC&app_version=6.5.0&device_id=34712926793&channel=App Store&mcc_mnc=46011&aid=1128&screen_width=750&openudid=263bd93f02801d126ca004edccbff8f6e1b19f51&os_api=18∾=WIFI&os_version=12.3.1&device_platform=iphone&build_number=65014&device_type=iPhone9,1&iid=74239983401&idfa=F39B285A-4B4F-4874-9D7E-C728A892BF6D"
    data = {"aweme_id": video_id}
    headers = {
        "sdk-version": "1",
        "x-Tt-Token": "00fc1e7950db67b5f43a312e9265cdfee513ea70c36d918c871f3bb553347f3db50ffca143b8722327b345816a75efca071d",
        "User-Agent": "Aweme 6.5.0 rv:65014 (iPhone; iOS 12.3.1; en_CN) Cronet",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "tt_webid=6636348554880222728; __tea_sdk__user_unique_id=6636348554880222728; odin_tt=76d9b82d6e6f2ddfc99719a5b5d44a7d703cf977f0f7bddf8537f93920d57cb9ec33162ee47868b760f6b09e69209bb2f90bad220b75678af850a0dfa9f056e2; install_id=74239983401; ttreq=1$dab0516952a4157c0c11d4993533c09d6e45fc94; sid_guard=fc1e7950db67b5f43a312e9265cdfee5%7C1559955316%7C5184000%7CWed%2C+07-Aug-2019+00%3A55%3A16+GMT; uid_tt=0afcb06309f632d872799ec0ac3b2c80; sid_tt=fc1e7950db67b5f43a312e9265cdfee5; sessionid=fc1e7950db67b5f43a312e9265cdfee5",
        "X-Khronos": "1559956401",
        "X-Gorgon": "8300000000002e40eee38cad71d14037bd1385d18bc973f094f5",
    }
    ret = {}
    res = requests.post(url, data=data, headers=headers)
    if res.status_code == 200:
        # tk_logger.info("video detail raw:%s" % res.content.decode("utf8"))
        jsn = json.loads(res.content)
        detail = jsn.get("aweme_detail", {})
        video_info = get_video_info(detail)
        user_info = get_user_info(detail)
        play_addr = get_play_address(detail)
        video_cover = get_video_cover(detail)
        ret["video_info"] = video_info
        ret["user_info"] = user_info
        ret["play_addr"] = play_addr
        ret["video_cover"] = video_cover
    else:
        raise Exception("get video detail failed [%s][%d]" % (url, res.status_code))
        return ret
