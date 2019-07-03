# 短时间休眠
import random
import time


def sleep_short():
    num = random.uniform(3, 5)
    time.sleep(num)


# 长时间休眠
def sleep_long():
    num = random.uniform(10, 20)
    time.sleep(num)
