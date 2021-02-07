import os

import cv2

"""
人脸识别功能
目的：监测硬件及第三方插件是否能正常监测到人脸。
"""

base_path = os.path.dirname(os.__file__)


class Detection(object):
    def __init__(self):
        # 开启摄像头
        print("开始获取摄像头数据...")
        self.cap = cv2.VideoCapture(0)
        print("开始显示摄像头数据...")
        # 人脸识别分类器
        self.faceCascade = cv2.CascadeClassifier(
            os.path.join(base_path, r'site-packages\cv2\data\haarcascade_frontalface_default.xml'))
        # 识别眼睛的分类器
        self.eyeCascade = cv2.CascadeClassifier(os.path.join(base_path, r'site-packages\cv2\data\haarcascade_eye.xml'))

    def start(self):
        ok = True
        while ok:
            # time.sleep(2)
            # 读取摄像头中的图像，ok为是否读取成功的判断参数
            ok, img = self.cap.read()
            # print("img", img)
            # 转换成灰度图像
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 人脸检测
            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=3,
                minSize=(20, 20)
            )
            print("faces", faces)
            result = []
            # 在检测人脸的基础上检测眼睛
            for (x, y, w, h) in faces:
                fac_gray = gray[y: (y + h), x: (x + w)]
                eyes = self.eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

                # 眼睛坐标的换算，将相对位置换成绝对位置
                for (ex, ey, ew, eh) in eyes:
                    result.append((x + ex, y + ey, ew, eh))

            # 画矩形
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            for (ex, ey, ew, eh) in result:
                cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('人脸检测', img)

            k = cv2.waitKey(1)
            if k == 27:  # press 'ESC' to quit
                break
        self.destroy()

    def destroy(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    det = Detection()
    det.start()
