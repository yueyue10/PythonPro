import datetime
import os
import time

import numpy as np


# 获取文件路径：https://www.cnblogs.com/dieyaxianju/p/6898254.html
def test_path():
    # base_path = os.path.dirname(os.__file__)
    # ss = os.path.join(base_path, 'site-packages\cv2\data\haarcascade_frontalface_default.xml')
    # print(ss)
    print(os.path.realpath(__file__))
    print(os.path.split(os.path.realpath(__file__)))
    print(os.getcwd())


# numpy.ndarray：https://www.runoob.com/numpy/numpy-array-attributes.html
def test_for():
    # --------第一种情况--------------
    # faces = (1, 2, 3)  # 类型：tuple
    # faces = [[311, 49, 181, 181]]  # 类型：list
    # print(type(faces))
    # --------第二种情况--------------
    # faces = np.arange(6)  # 类型:numpy.ndarray
    faces = np.array([[1, 2, 3], [4, 5, 6]])
    print(faces, faces.ndim, faces.shape, faces.shape[0])
    if type(faces) == tuple and faces:
        print('属于：tuple类型，且非空')
    elif type(faces) == np.ndarray and faces.any():
        print('属于：ndarray类型，且非空')


def test_time():
    t = time.time()
    print(t)  # 原始时间数据
    print(int(t))  # 秒级时间戳 1612678163 1612678190
    print(int(round(t * 1000)))  # 毫秒级时间戳
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 日期格式化


if __name__ == '__main__':
    # test_path()
    # test_for()
    test_time()
