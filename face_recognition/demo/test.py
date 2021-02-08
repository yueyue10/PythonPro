import datetime
import os
import threading
import time

import numpy as np
from pywebio.input import *
from pywebio.output import *


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


def test_dir():
    path = "face_data"
    image_paths = []
    for f in os.listdir(path):
        image_paths.append(os.path.join(path, f))
    print("image_paths", image_paths)
    for imagePath in image_paths:
        image_name = os.path.split(imagePath)[-1]
        name = image_name.split(".")[0]
        id_pre = image_name.split(".")[1]
        print(image_name, "      ", name, "      ", id_pre)


class TimerTest(object):
    def __init__(self):
        print("主进行1")
        self.create_timer()
        print("主进行2")
        print("主进行3")
        print("主进行...")

    def create_timer(self):
        print("开始：", time.strftime('%H:%M:%S', time.localtime()))
        t = threading.Timer(2, self.repeat)
        t.start()

    @staticmethod
    def repeat():
        print('结束：', time.strftime('%H:%M:%S', time.localtime()))
        # create_timer()


class LoadingTest(object):
    def __init__(self):
        self.show_loading()

    def show_loading(self, timeout=5):
        print('show_loading------------')
        with use_scope('loading'):
            put_loading(color="primary")
            put_text("加载中...")
            put_html("""<style>                                           
                        #pywebio-scope-loading {border: 1px solid red;text-align:center}
                        </style>
                        <br/>
                        """)
        # loading = threading.Timer(timeout, self.hide_loading)
        # loading.start()

    def hide_loading(self):
        print("hide_loading--------------")
        clear(scope='loading')


if __name__ == '__main__':
    # test_path()
    # test_for()
    # test_time()
    # test_dir()
    # timer = TimerTest()
    load = LoadingTest()
