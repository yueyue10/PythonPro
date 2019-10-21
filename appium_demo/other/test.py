import json
import threading
import time

import requests

from other import json_data
from other.visitors.mogu_visitor import headers


def json_test():
    # 将字典转化成JSON来发送
    data_json = json.dumps(json_data)
    print(data_json)


def request():
    req = requests.get("http://localhost:8762/hi", headers=headers, timeout=5)
    print("json数据__%s__>>" % 'json', req.content)


def json_request():
    # 完成所有线程分配，并不立即开始执行
    threads = []
    for i in range(0, 100):
        t = threading.Thread(target=request)
        threads.append(t)
    for t in threads:
        t.start()
        time.sleep(1)


if __name__ == '__main__':
    # json_test()
    json_request()

# http://pingma.qq.com:80/mstat/report/?index=1571030636

