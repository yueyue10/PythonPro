import datetime
import time

from pywebio.input import *
from pywebio.output import *

from demo import conf
from demo.face_data_collect import Collection
from demo.face_recognition import Recognition
from demo.face_training import Training


class FaceTools:
    def __init__(self):
        self.put_title("人脸识别功能", num=1, center=True)

    def start(self):
        collect_info = input_group('第一步：采集人脸数据', [
            input('face_num', type=NUMBER, name='face_num', required=True, value=10),
            actions('action', [
                {'label': '开始采集', 'value': 'start'}
            ], name='action', help_text='actions'),
        ])
        if collect_info['action'] == 'start':
            self.collect(collect_info['face_num'])
        confirm = actions('第二步：人脸数据训练', ['开始训练'], help_text='训练人脸数据')
        if confirm == '开始训练':
            self.training()
        confirm = actions('第三步：人脸检测功能', ['开始检测'], help_text='检测人脸功能')
        if confirm == '开始检测':
            self.recognition()

    def collect(self, num):
        self.put_title('第一步：采集人脸数据')
        self.put_text("正在打开电脑相机，请稍后>>>")
        collection = Collection(face_name='zyj', face_id=1000)
        self.put_text("开始获取摄像头数据...")
        self.put_text('按下Esc可以退出')
        collection.save_user_pictures(total_count=num)
        self.put_text('采集完成')
        self.put_title('人脸数据：', num=5)
        for face_img in conf.face_images:
            put_image(face_img, width='100px')

    def training(self):
        self.put_title('第二步：人脸数据训练')
        self.put_text('开始训练人脸模型，需要一点时间，等稍等...')
        train = Training()
        train.start()
        time.sleep(5)
        self.put_text("{} 个人脸模型训练完成！".format(len(conf.face_dict)))

    def recognition(self):
        self.put_title('第三步：人脸检测功能')
        self.put_text('正在打开电脑相机，请稍后>>>')
        recognition = Recognition()
        self.put_text("开始获取摄像头数据...")
        self.put_text('按下Esc可以退出')
        recognition.start()
        self.put_text('识别完成')

    def count_t(self, num):
        start_time = datetime.datetime.now()
        while True:
            end_time = datetime.datetime.now()
            if (end_time - start_time).seconds == num:
                print("pass 5 seconds!")

    @staticmethod
    def put_title(title, num=3, center=False):
        if center:
            style(put_html('<h{1}>{0}</h{1}>'.format(title, num)), 'text-align:center')
        else:
            put_html('<h{1}>{0}</h{1}>'.format(title, num))

    @staticmethod
    def put_text(text):
        put_html('<p>{}</p>'.format(text))


if __name__ == '__main__':
    face = FaceTools()
    face.start()
