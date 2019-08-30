#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/29 16:50
# @Author  : cjf
# @Site    : 时间格式转化
# @File    : timeUtil.py
# @Software: PyCharm

import sys

sys.path.append('..')
from datetime import datetime, date, timedelta
# time 格式转换
import time


def format_time(timestr, format1, format2):
    '''
      %d/%m/%Y %H:%M >> %Y年%m月%d日
      16/06/2017 07:54
      format_time('16/06/2017 07:54','%d/%m/%Y %H:%M','%Y年%m月%d日 %H:%M')
    :param format1: original time format
    :param format2: target time format
    :param timestr: original time string
    :return:
    '''
    return time.strftime(format2, time.strptime(timestr, format1))


# return now timestamp
def now_timestamp():
    return int(time.time())


# return timestamp_to_13
def timestamp_to_13():
    num_ = time.time()
    time_ = int(num_ * 1000)
    return time_


# return now time(date)
def now_datetime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def now_datetime_no():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def now_month_no():
    return time.strftime("%Y-%m", time.localtime(time.time()))


# timestamp to time(date)
def timestamp_to_str(ctime):
    tmp_time = time.localtime(int(ctime))
    ctimeStr = time.strftime("%Y-%m-%d %H:%M:%S", tmp_time)
    return ctimeStr


# time(date) to timestamp
def timestr_to_timestamp(s):
    return int(time.mktime(time.strptime(s, '%Y-%m-%d %H:%M:%S')))


# return n day sec 10:59-->659
def durationTosecs(video_duration):
    global dur
    if video_duration and ':' in video_duration:
        video_duration = video_duration.split(':')
        min = video_duration[0]
        min = int(min) * 60
        sec = video_duration[1]
        sec = int(sec)
        dur = min + sec
    else:
        print("video_duration get filed, return 0")
        dur = 0
    return dur


def format_string_datetime(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')


def dateTimeToTimestamplong(format_info):
    dtime = format_string_datetime(format_info)
    un_time = int(time.mktime(dtime.timetuple())) * 1000
    return un_time


def getDatetimeToday():
    t = date.today()  # date类型
    dt = datetime.strptime(str(t), '%Y-%m-%d')  # date转str再转datetime
    return dt


# 获取前一天日期
def getDatetimeYesterday():
    today = getDatetimeToday()  # datetime类型当前日期
    yesterday = today + timedelta(days=-1)  # 减去一天
    yesterday = str(yesterday).replace("00:00:00", "").strip()
    return yesterday


# 获取明天日期
def getDatetimeNextday():
    today = getDatetimeToday()  # datetime类型当前日期
    nextday = today + timedelta(days=+1)  # 加一天
    nextday = str(nextday).replace("00:00:00", "").strip()
    return nextday


# 获取明天日期
def getDatetimeAppoint(num):
    today = getDatetimeToday()  # datetime类型当前日期
    nextday = today + timedelta(days=-int(num))  # 加一天
    nextday = str(nextday).replace("00:00:00", "").strip()
    return nextday


# 获取20天日期
def getDatetimeNext30day():
    today = getDatetimeToday()  # datetime类型当前日期
    nextday = today + timedelta(days=+20)  # 加一天
    nextday = str(nextday).replace("00:00:00", "").strip()
    return nextday


# 获取后天日期
def getDatetimeNextNextday():
    today = getDatetimeToday()  # datetime类型当前日期
    nextday = today + timedelta(days=+2)  # 加一天
    nextday = str(nextday).replace("00:00:00", "").strip()
    return nextday
