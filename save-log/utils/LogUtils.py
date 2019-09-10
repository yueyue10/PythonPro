# coding=utf-8
# __author__ = 'wangning'


import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

sys.path.append('..')
logger_dict = {}


class Logs(object):

    def __init__(self, log_name):
        if log_name not in logger_dict:
            log = logging.getLogger()
            formatter = logging.Formatter(
                '%(asctime)-12s level-%(levelname)-8s thread-%(thread)-8d %(message)s')  # 每行日志的前缀设置
            fileTimeHandler = TimedRotatingFileHandler(log_dir + str(log_name), when="M", interval=15, backupCount=288)

            # fileTimeHandler.suffix = "%Y-%m-%d_%H"  #设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
            # fileTimeHandler.setFormatter(formatter)
            logging.basicConfig(level=logging.NOTSET)
            fileTimeHandler.setFormatter(formatter)
            log.addHandler(fileTimeHandler)
            logger_dict[log_name] = log
        self.log = logger_dict[log_name]

    def error(self, e, message):
        self.log.error(message)
        print(message)

    def debug(self, message):
        self.log.debug(message)

    def info(self, message):
        self.log.info(message)
        print(message)

    def warning(self, message):
        self.log.warning(message)

    def critical(self, message):
        self.log.critical(message)


log_dir = os.path.abspath('.')
# log_dir = 'E:/Users/Python/data/logs/'
Log = Logs('save_log.log')
