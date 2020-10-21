import json

import requests


class UserLikeVideos:
    headers = {"Accept": "application/json",
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36',
               'Cookie': '_ga=GA1.2.221321654.1571713017; _gid=GA1.2.1458812847.1571713017; tt_webid=6750458410351052291; _ba=BA0.2-20191022-5199e-7SquHfJeofJqN8tybc8u',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               "X-Requested-With": "XMLHttpRequest",
               }
    # 预置的参数，正常情况是固定的
    like_url = 'https://www.iesdouyin.com/web/api/v2/aweme/like/?'
    # 不变的参数
    _dytk = r'ac5e995179f3a8a16d1f5e7266ea6a08'
    # 分页的页码标识，暂时无法破解，这里是预置进去的。也就是从浏览器获取之后保存到cursors.txt中的，测试发现是不变的。具体可能还得用自己的浏览器获取
    _cursor_path = 'cursors.txt'
    # 全部视频列表数据保存路径(data.txt当作备份文件了，真正使用了data.json中的数据，其实两者是一样的。因为data.json中有自己手动添加的数据)
    _video_data_path = 'data.txt'

    def __init__(self, _user_id, _signstr, _cookie):
        self._user_id = _user_id
        self._signstr = _signstr
        print('sign:%s   dytk:%s' % (_signstr, self._dytk))
        self.headers["Cookie"] = _cookie
        self.save_video_ids()

    # 保存all_video[desc:视频名称, aweme_id:视频id]数据到文件中
    def save_video_ids(self):
        # cursors = self.get_cursor()
        # 这次不再手动保存cursor数据，请求第一条后，从返回之里面获取到cursor
        all_video = []
        cursor_idx = 0
        while (cursor_idx >= 1572436867000) or (cursor_idx == 0):
            videos, max_cursor = self.get_video_json_data(cursor_idx)
            cursor_idx = max_cursor
            all_video = all_video + videos
        print("\n视频总条数：%d条" % len(all_video))
        with open(self._video_data_path, 'w', encoding='utf-8') as f:
            f.write(str(all_video))
        print("保存视频名称和ID数据到data.txt成功")

    # 获取cursor分页标识方法
    def get_cursor(self):
        with open(self._cursor_path, 'r', encoding='utf-8') as f:
            _cursors = f.readlines()
        _cursors = [c.replace('\n', '') for c in _cursors]
        print("\n获取cursors数据成功", "共%d页\n" % len(_cursors))
        return _cursors

    # 解析 get_user_like_video_list_by_uid 接口获取视频列表数据
    def get_video_json_data(self, cursor_id=0):
        json_str = self.get_user_like_video_list_by_uid(cursor_id)
        data = json_str['aweme_list']
        data_length = len(data)
        if data_length:
            print("数据获取成功，因为内容太长这里不显示了", "---->数据长度：", data_length, "\n")
        else:
            print("_cursor=### %s ###页没获取到数据：" % str(cursor_id))
            print(json_str, "---->数据长度：", data_length, "\n")
        max_cursor = json_str['max_cursor']
        videos = []
        for aweme in json_str['aweme_list']:
            aweme_id = aweme["aweme_id"]  # 视频id
            desc = aweme["desc"]  # 视频描述
            videos.append([desc, aweme_id])
        return videos, max_cursor

    # 获取用户收藏的视频列表
    def get_user_like_video_list_by_uid(self, _cursor=0):
        if self._signstr is None or self._dytk is None:
            print("sign [%s] or dytk [%s] is none" % (self._signstr, self.dytk))
            return None
        params = {
            "user_id": self._user_id,
            "count": "21",
            "max_cursor": _cursor,
            "aid": "1128",
            "_signature": self._signstr,
            "dytk": self._dytk
        }
        res = requests.get(self.like_url, headers=self.headers, params=params)
        print("params", params)
        content = res.content.decode("utf8")
        # print("content" + content)
        jsn = json.loads(content)
        return jsn


if __name__ == '__main__':
    # 用户id
    m_user_id = '104713356413'
    # QueryStringParameters里面的参数_signature
    _signature = r'qxrjthAd9U5DwMHLLuUJMqsa46'
    # RequestHeader里面的参数cookie
    Cookie = r"_ga=GA1.2.221321654.1571713017; tt_webid=6750458410351052291; _ba=BA0.2-20191022-5199e-7SquHfJeofJqN8tybc8u; _gid=GA1.2.678761716.1579497260"
    userlikevideos = UserLikeVideos(m_user_id, _signature, Cookie)
    # 我这里正常情况下是882条，如果少了一点也是正常的。因为视频列表的里面的视频可能被作者删除了。
    # 以后完善的话，可以使用selenium的webdriver请求url地址获取到上面的 cookie 和 _signstr 值，以及保存到文件中的 cursor 值。

# https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=104713356413&sec_uid=&count=21&max_cursor=0&aid=1128&_signature=qxrjthAd9U5DwMHLLuUJMqsa46&dytk=ac5e995179f3a8a16d1f5e7266e
