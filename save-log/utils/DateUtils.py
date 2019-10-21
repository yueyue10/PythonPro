import datetime
import time


def test():
    d1 = datetime.datetime(2009, 10, 23)
    d2 = datetime.datetime(2009, 10, 7)
    dayCount = (d1 - d2).days

    print(dayCount)


def test1():
    starttime = datetime.datetime.now()
    time.sleep(4)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)


def test2():
    d1 = datetime.datetime.now()
    d3 = d1 + datetime.timedelta(days=10)
    print(d3.ctime())


def test3(time1='2017-10-16 19:21:22', time2='2017-10-17 20:22:22'):
    # 计算两个时间的间隔
    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    print(d1)
    print(d2)
    days = (d2 - d1).days
    seconds = (d2 - d1).seconds
    print(days)
    print(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print("%02d天%02d小时%02d分钟%02d秒" % (days, h, m, s))


def test4():
    # 日期转成时间戳
    # 计算时间戳差值
    time1 = time.strptime('2019-09-11 08:00:37', "%Y-%m-%d %H:%M:%S")
    time2 = time.strptime('2019-09-11 08:49:10', "%Y-%m-%d %H:%M:%S")
    timeStamp1 = int(time.mktime(time1))
    timeStamp2 = int(time.mktime(time2))
    print(timeStamp1)
    print(timeStamp2)
    print(timeStamp2 - timeStamp1)


if __name__ == '__main__':
    # test()
    # test1()
    # test2()
    # test3('2019-09-09 00:19:46', '2019-09-10 00:20:11')
    test4()
