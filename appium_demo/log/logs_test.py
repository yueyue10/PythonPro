import logging
import os
from logging import handlers

from appium_demo.log import LogConfig, save_log
from appium_demo.log.logger import MyLog


class TestLogger(object):

    def __init__(self, filename, when='D', back_count=3, console=True):
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别
        th = handlers.TimedRotatingFileHandler(filename=os.path.join(LogConfig.log_path, filename), when=when,
                                               backupCount=back_count, encoding='utf-8')
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，
        # when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        format_str = logging.Formatter(LogConfig.fmt_style)  # 设置日志格式
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th.setFormatter(format_str)  # 设置文件里写入的格式
        if console: self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


class TestLog:

    def __init__(self, console=False):
        self.all_log = TestLogger("all_log.log", console=console).logger
        self.err_log = TestLogger("err_log.log", console=console).logger

    def d(self, info):
        self.all_log.debug(info)

    def i(self, info):
        self.all_log.info(info)

    def w(self, info):
        self.all_log.warning(info)

    def e(self, info):
        self.err_log.error(info)

    def c(self, info):
        self.err_log.critical(info)


# test_log = TestLog("test_log.log")
#
#
# def d(info):
#     test_log.logger.debug(info)

# def test():
#     MyLog.info('This is info')
#     MyLog.warning('This is warning')
#     MyLog.error('This is error')


if __name__ == '__main__':
    # 测试代码一：
    # d("dddd")
    # 测试代码二：
    # log = TestLog(console=True)
    # log.d("haha")
    # log.e("error")
    # 测试代码三:可以保存到固定位置,可是日志定位是logger/logger.py
    # test()
    # logging.error("输出12")
    save_log(1, '2')
