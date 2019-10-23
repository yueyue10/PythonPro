#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock

from requests import get, head

lock = Lock()


class Downloader():
    def __init__(self, url, nums, file):
        self.url = url
        self.num = nums
        self.name = file
        r = head(self.url)
        # 若资源显示302,则迭代找寻源文件
        while r.status_code == 302:
            self.url = r.headers['Location']
            print("该url已重定向至{}".format(self.url))
            r = head(self.url)
        self.size = int(r.headers['Content-Length'])
        print('该文件大小为：{} bytes'.format(self.size))

    def down(self, start, end):
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        # stream = True 下载的数据不会保存在内存中
        r = get(self.url, headers=headers, stream=True)
        # 写入文件对应位置,加入文件锁
        lock.acquire()
        with open(self.name, "rb+") as fp:
            fp.seek(start)
            fp.write(r.content)
            lock.release()
            # 释放锁

    def run(self):
        # 创建一个和要下载文件一样大小的文件
        fp = open(self.name, "wb")
        fp.truncate(self.size)
        fp.close()
        # 启动多线程写文件
        part = self.size // self.num
        pool = ThreadPoolExecutor(max_workers=self.num)
        futures = []
        for i in range(self.num):
            start = part * i
            # 最后一块
            if i == self.num - 1:
                end = self.size
            else:
                end = start + part - 1
                print('{}->{}'.format(start, end))
            futures.append(pool.submit(self.down, start, end))
        wait(futures)
        print('%s 下载完成' % self.name)