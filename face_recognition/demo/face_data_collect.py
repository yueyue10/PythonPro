import os
import time
import cv2
import numpy as np

"""
人脸数据收集
"""
base_path = os.path.dirname(os.__file__)

width = 640
height = 480
h_wid = int(width / 2)
h_hei = int(height / 2)


class Collection:

    def __init__(self, face_id):
        self.face_detector = cv2.CascadeClassifier(
            os.path.join(base_path, r'site-packages\cv2\data\haarcascade_frontalface_default.xml'))
        self.dir_path = self.init_dir(face_id)
        print("开始获取摄像头数据...")
        # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
        self.cap = cv2.VideoCapture(0)
        print("开始加载摄像头数据...")
        self.pic_count = 0  # 照片编号初始值
        self.can_save = True  # 是否可以保存图片
        self.time_cache = None  # 记录保存图片的时间戳缓存
        self.save_user_pictures()

    @staticmethod
    def init_dir(face_id):
        m_path = os.getcwd()
        # 本地保存图片根路径（请确保根路径存在）
        dir_path = os.path.join(m_path, r'face_data\user{}'.format(face_id))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        return dir_path

    # 保存一定数量的照片
    def save_user_pictures(self, total_count=10):
        self.cap.set(3, width)  # set video width
        self.cap.set(4, height)  # set video height
        print('\n 看着摄像机获取照片...')
        while True:
            # 从摄像头读取图片
            success, img = self.cap.read()
            # print("img", img)
            # 转为灰度图片
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 检测人脸
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

            # print("faces=====", faces, type(faces))
            if type(faces) == np.ndarray and faces.any():  # 如果数据类型是：numpy.ndarray并且数据不为空
                self.draw_rect(img, faces, gray)
            else:
                if not self.can_save:
                    cv2.putText(img, "saving {} picture".format(self.pic_count), (h_wid - 50, h_hei),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (208, 2, 27), 1)
                    print("保存图片中...")
                else:
                    cv2.putText(img, "no face data,look the camera", (h_wid - 150, h_hei), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (144, 19, 254), 1)
                    print("没有识别到人脸信息，请正对摄像头...")
            self.timer()
            cv2.imshow('人脸数据收集', img)
            # 保持画面的持续
            k = cv2.waitKey(1)
            if k == 27:  # 通过esc键退出摄像
                break
            elif self.pic_count >= total_count:  # 得到1000个样本后退出摄像
                break
        self.destroy()

    def draw_rect(self, img, faces, gray):
        show_text = faces.shape[0] == 1  # 人脸等于1
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
            if show_text and self.can_save:  # 如果只有一个人脸并且可以保存的时候，保存图片
                self.save_pics(faces, gray)
            else:
                cv2.putText(img, "here is one more face,keep one face", (h_wid - 100, h_hei), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (144, 19, 254), 1)

    def save_pics(self, faces, gray):
        # 这个方法调用前保证了faces里面只有一个元素，这里只是取出二维数组里面的元素
        for (x, y, w, h) in faces:
            self.save_pic(gray[y: y + h, x: x + w])

    def save_pic(self, gray_data):
        self.pic_count += 1
        # 保存图像
        file_path = '%s/%s%s' % (self.dir_path, str(self.pic_count), '.jpg')
        cv2.imwrite(file_path, gray_data)
        self.timer(start=True)

    def timer(self, start=False):
        cur_time = int(time.time())
        print("cur_time", cur_time)
        if self.time_cache and cur_time - self.time_cache >= 3:
            self.time_cache = None
            self.can_save = True
        elif start:
            self.time_cache = cur_time
            self.can_save = False

    def destroy(self):
        # 关闭摄像头
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    collection = Collection(1)
