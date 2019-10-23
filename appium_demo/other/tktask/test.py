import json

import requests

from other.tktask.down import SeleniumClient

headers = {"Accept": "application/json",
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
           'Cookie': '_ga=GA1.2.221321654.1571713017; _gid=GA1.2.1458812847.1571713017; tt_webid=6750458410351052291; _ba=BA0.2-20191022-5199e-7SquHfJeofJqN8tybc8u',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           "X-Requested-With": "XMLHttpRequest",
           }


def get_user_video_list_by_uid(user_id, cursor=0):
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/like/?'
    dytk = r'ac5e995179f3a8a16d1f5e7266ea6a08'
    print("sign:%s,dytk:%s" % (signstr, dytk))
    if signstr is None or dytk is None:
        print("sign [%s] or dytk [%s] is none" % (signstr, dytk))
        return None
    params = {
        "user_id": user_id,
        "count": "21",
        "max_cursor": cursor,
        "aid": "1128",
        "_signature": signstr,
        "dytk": dytk
    }
    res = requests.get(url, headers=headers, params=params)
    try:
        print.info("request url: %s" % res.url)
    except:
        pass
    content = res.content.decode("utf8")
    # print("content" + content)
    jsn = json.loads(content)
    return jsn


def get_cursor():
    with open('cursors.txt', 'r', encoding='utf-8') as f:
        cursors = f.readlines()
    cursors = [c.replace('\n', '') for c in cursors]
    print("获取cursors数据成功", len(cursors))
    return cursors


def get_aweme_ids(cursor_id=0):
    jsonStr = get_user_video_list_by_uid(user_id, cursor=cursor_id)
    # print(jsonStr)
    data = jsonStr['aweme_list']
    print("\n\n\n数据长度：", len(data))
    aweme_ids = []
    for aweme in jsonStr['aweme_list']:
        aweme_id = aweme["aweme_id"]
        desc = aweme["desc"]
        aweme_ids.append([desc, aweme_id])
    return aweme_ids


if __name__ == '__main__':
    cursors = get_cursor()
    user_id = '104713356413'
    signstr = r'BR0UlBAeWLntxzbpp7YCEgUdFI'
    headers[
        "Cookie"] = r"_ga=GA1.2.221321654.1571713017; _gid=GA1.2.1458812847.1571713017; tt_webid=6750458410351052291; _ba=BA0.2-20191022-5199e-7SquHfJeofJqN8tybc8u"
    all_video = []
    for cursor in cursors:
        video_ids = get_aweme_ids(cursor)
        all_video = all_video + video_ids
    print("总数据长度：", len(all_video))
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write(str(all_video))
