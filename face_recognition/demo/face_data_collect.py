import os
import time

import cv2

"""
人脸数据收集
"""


class Collection:

    def __init__(self, path):
        self.face_detector = cv2.CascadeClassifier(
            r'E:\Users\Python\Libs\FaceIdentify\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
        # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)  # set video width
        self.cap.set(4, 480)  # set video height
        self.path = path

    # 保存一定数量的照片
    def save_user_pictures(self, total_count):
        print('\n 看着摄像机获取照片...')
        # 照片编号初始值
        count = 0
        while True:
            time.sleep(2)
            # 从摄像头读取图片
            success, img = self.cap.read()
            # print("img", img)
            # 转为灰度图片
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 检测人脸
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
                count += 1
                # 保存图像
                file_path = '%s/%s%s' % (self.path, str(count), '.jpg')
                cv2.imwrite(file_path, gray[y: y + h, x: x + w])
                cv2.imshow('image', img)

            # 保持画面的持续。
            k = cv2.waitKey(1)
            if k == 27:  # 通过esc键退出摄像
                break
            elif count >= total_count:  # 得到1000个样本后退出摄像
                break
        # 关闭摄像头
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # For each person, enter one numeric face id
    # face_id = input('采集用户数据，输入用户的id编号(数字):')
    face_id = "1"

    # 本地保存图片根路径（请确保根路径存在）
    dir_path = r'E:\Users\Python\PythonPro\face_recognition\demo\facedata\user' + face_id
    if not os.path.exists(dir_path):
        os.path.join(dir_path)
        os.mkdir(dir_path)
    collection = Collection(dir_path)
    collection.save_user_pictures(10)
