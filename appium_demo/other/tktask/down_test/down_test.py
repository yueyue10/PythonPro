#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getopt import GetoptError, getopt
from sys import argv, exit
from time import time

from downloader import Downloader

usage = """
用法： ./dam.py [<地址>] [-n <选项>] [-o <选项>]
url                      None     指定下载链接
num-connection=x         -n x     指定连接数目（即线程数）
outputfile=f             -o f     指定输出本地文件
help                     -h       帮助信息
version                  -v       版本信息
"""

version = """
版本 1.1 (Linux)
Copyright 2017 Wincer
详细信息阅读 CREDITS 文件
"""


def main(argv):
    try:
        if argv[0] not in ('-v', '-h'):
            inputurl = argv[0]
            argv = argv[1:]
        else:
            inputurl = ''
        numthread = ''
        outputfile = ''
        opts, args = getopt(argv, "hvn:o:")
    except GetoptError:
        print(usage)
        exit(2)
    except IndexError:
        print(usage)
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            exit()
        elif opt == '-v':
            print(version)
            exit()
        elif opt == "-n":
            numthread = arg
        elif opt == "-o":
            outputfile = arg
    print('输入的url为：{}'.format(inputurl))
    print('输出的文件名为：{}'.format(outputfile))
    return inputurl, numthread, outputfile


if __name__ == "__main__":
    # url, nums, file = main(argv[1:])
    url = "http://v3-dy.ixigua.com/fe931ac6b035e84317cb399bbfd58af9/5daffe5d/video/m/220a8a6d53d7217425c947f273e5cfe7c6f1161a66d400007ed40767c5c7/?a=1128&br=2232&cr=0&cs=0&dr=0&ds=3&er=&l=201910231416330100140381670826C2&lr=aweme&qs=0&rc=aml2PDg3bWt0bDMzZ2kzM0ApO2k5PDZkZWRoN2Y0OGY4OmdfMGMtcWZpZDRfLS1fLTBzczM2YTYvXzVeMV9hMDAzMi86Yw%3D%3D"
    nums = 5
    file = "测试视频.mp4"
    start = time()
    if nums == '':
        # 若用户没有输入进程数，则设置默认进程数4
        nums = 4
    if file == '':
        # 若用户没有输入文件名，则产生随机文件名
        file = 'File' + str(int(time() % 10))
    try:
        down = Downloader(url, int(nums), file)
        down.run()
    except Exception as e:
        print(e)
        exit(2)
    end = time()
    print("用时: {times}, 平均速度: {speed:.2f}KB/s.".format(
        times=end - start, speed=down.size / (end - start)))
