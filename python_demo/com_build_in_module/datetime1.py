from datetime import datetime, timedelta, timezone

print('''---------------------datetime---------------------
''')
# datetime是Python处理日期和时间的标准库。

# *********** 获取当前日期和时间 ***********
# 我们先看如何获取当前日期和时间：
now = datetime.now()  # 获取当前datetime
print(now)
print(type(now))

# *********** 获取指定日期和时间 ***********
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print("\n获取指定日期和时间", dt)

# *********** datetime转换为timestamp ***********
# 在计算机中，时间实际上是用数字表示的。
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print("\ndatetime转换为timestamp", dt.timestamp())  # 把datetime转换为timestamp
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

# *********** timestamp转换为datetime ***********
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t = 1429417200.0
print("\ntimestamp转换为datetime# 本地时间", datetime.fromtimestamp(t))
print("timestamp转换为datetime# UTC时间", datetime.utcfromtimestamp(t))

# *********** str转换为datetime ***********
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print("\nstr转换为datetime", cday)
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档。

# *********** datetime转换为str ***********
now = datetime.now()
print("\ndatetime转换为str", now.strftime('%Y-%m-%d %H:%M:%S'))

# *********** datetime加减 ***********
now = datetime.now()
print("\nnow + timedelta(hours=10)=", now + timedelta(hours=12))
print("now - timedelta(days=1)=", now - timedelta(days=1))
print("now + timedelta(days=2, hours=12)=", now + timedelta(days=2, hours=12))
# 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

# *********** 本地时间转换为UTC时间 ***********
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print("\nnow.replace(tzinfo=tz_utc_8)=", now.replace(tzinfo=tz_utc_8))

# *********** 时区转换 ***********
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 拿到UTC时间，并强制设置时区为UTC+0:00:
print("\nutc_dt=", utc_dt)
