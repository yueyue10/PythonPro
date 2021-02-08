import datetime
import threading
import time

from pywebio.input import *
from pywebio.output import *

from demo import conf
from demo.face_data_collect import Collection
from demo.face_recognition import Recognition
from demo.face_training import Training


class FaceApp:
    def __init__(self):
        self.put_title("人脸识别功能", t_size=1, center=True)

    def start(self):
        coll_info = input_group('第一步：采集人脸数据', [
            input('face_name', type=TEXT, name='face_name', required=True, placeholder="请输入人脸名称，请使用英文标识"),
            input('face_num', type=NUMBER, name='face_num', required=True, placeholder="请输入采集人脸数量", value=5),
            actions('action', [
                {'label': '开始采集', 'value': 'start'}
            ], name='action', help_text='actions'),
        ])
        if coll_info['action'] == 'start':
            self.collect(coll_info['face_num'], coll_info['face_name'])
        confirm = actions('第二步：人脸数据训练', ['开始训练'], help_text='训练人脸数据')
        if confirm == '开始训练':
            self.training()
        confirm = actions('第三步：人脸检测功能', ['开始检测'], help_text='检测人脸功能')
        if confirm == '开始检测':
            self.recognition()

    def collect(self, face_num, face_name):
        self.put_title('第一步：采集人脸数据')
        self.show_loading(timeout=7)
        self.put_text_delay("正在打开电脑相机，请稍后>>>")
        collection = Collection(face_name=face_name, face_id=1000)
        self.put_text_delay("开始获取摄像头数据...", timeout=2)
        self.put_text_delay("开始加载视频窗口...", timeout=4)
        self.put_text_delay('按下Esc可以退出', timeout=6)
        collection.save_user_pictures(total_count=face_num)
        self.put_text('采集完成')
        self.put_title('人脸数据：', t_size=5)
        for face_img in conf.get_face_images():
            put_image(face_img, width='100px')

    def training(self):
        self.put_title('第二步：人脸数据训练')
        self.show_loading()
        self.put_text('开始训练人脸模型，需要一点时间，等稍等...')
        train = Training()
        train.start()
        time.sleep(3)
        self.put_text("{} 个人脸模型训练完成！".format(len(conf.get_face_dict())))

    def recognition(self):
        self.put_title('第三步：人脸检测功能')
        self.put_text_delay('正在打开电脑相机，请稍后>>>')
        self.show_loading(timeout=3)
        recognition = Recognition()
        self.put_text("开始获取摄像头数据...")
        self.put_text_delay('按下Esc可以退出')
        recognition.start()
        self.put_text('识别完成')

    def show_loading(self, timeout=5):
        print('show_loading------------')
        with use_scope('loading'):
            put_loading(color="primary")
            put_text("加载中...")
            put_html("""<style>#pywebio-scope-loading {text-align:center}</style>""")
        timer = threading.Timer(timeout, self.hide_loading)
        timer.start()

    @staticmethod
    def hide_loading():
        print("hide_loading--------------")
        remove(scope='loading')

    @staticmethod
    def put_title(title, t_size=3, center=False):
        if center:
            style(put_html('<h{1}>{0}</h{1}>'.format(title, t_size)), 'text-align:center')
        else:
            put_html('<h{1}>{0}</h{1}>'.format(title, t_size))

    def put_text_delay(self, text, timeout=2):
        timer = threading.Timer(timeout, self.put_text, [text])
        timer.start()

    @staticmethod
    def put_text(text):
        put_html('<p>{}</p>'.format(text))


if __name__ == '__main__':
    app = FaceApp()
    app.start()
