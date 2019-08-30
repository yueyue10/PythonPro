# coding: utf-8

import logging.handlers
import os
import sys

from lxml import etree

# 提供日志功能
from appium_demo.log import LogConfig


class MyLog:
    # 先读取XML文件中的配置数据
    # 由于config.xml放置在与当前文件相同的目录下，因此通过 __file__ 来获取XML文件的目录，然后再拼接成绝对路径
    # 这里利用了lxml库来解析XML
    root = etree.parse(os.path.join(os.path.dirname(__file__), 'config.xml')).getroot()
    # 读取日志文件保存路径
    log_path = root.find('logpath').text
    # 读取日志文件容量，转换为字节
    log_size = 1024 * 1024 * int(root.find('logsize').text)
    # 读取日志文件保存个数
    log_num = int(root.find('lognum').text)
    # 日志文件名：由用例脚本的名称，结合日志保存路径，得到日志文件的绝对路径
    log_name = os.path.join(log_path, sys.argv[0].split('/')[-1].split('.')[0])

    # 初始化logger
    log = logging.getLogger()
    # 日志格式，可以根据需要设置
    fmt = logging.Formatter(LogConfig.fmt_style)

    # 日志输出到文件，这里用到了上面获取的日志名称，大小，保存个数
    handle1 = logging.handlers.RotatingFileHandler(log_name, maxBytes=log_size, backupCount=log_num)
    handle1.setFormatter(fmt)
    # 同时输出到屏幕，便于实施观察
    handle2 = logging.StreamHandler(stream=sys.stdout)
    handle2.setFormatter(fmt)
    log.addHandler(handle1)
    log.addHandler(handle2)

    # 设置日志基本，这里设置为INFO，表示只有INFO级别及以上的会打印
    log.setLevel(logging.INFO)

    # 日志接口，用户只需调用这里的接口即可，这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口
    @classmethod
    def info(cls, msg):
        cls.log.info(msg)
        return

    @classmethod
    def warning(cls, msg):
        cls.log.warning(msg)
        return

    @classmethod
    def error(cls, msg):
        cls.log.error(msg)
        return
