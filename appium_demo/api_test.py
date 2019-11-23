import time

import requests

headers = {
    "token": "XZ_DXG_1574412122440002_9S88E3"
}
params = {
    "user_id": 1
}

links = [
    "http://genius.enn.cn/xz-dxg-report/home/enter-count",
    "http://genius.enn.cn/xz-dxg-report/home/dispense",
    "http://genius.enn.cn/xz-dxg-report/home/forecast",
    "http://genius.enn.cn/xz-dxg-report/home/bus-sum",
    "http://genius.enn.cn/xz-dxg-report/home/usable-power",
    "http://genius.enn.cn/xz-dxg-report/home/dinner-sum"
]


def request_test():
    for index, like_url in enumerate(links):
        res = requests.get(like_url, headers=headers, params=params, timeout=10)
        # time.sleep(1)
        content = res.content.decode("utf8")
        print("---------------------第%s个接口---------------------\n" % (index + 1), res, content)


if __name__ == '__main__':
    request_test()
