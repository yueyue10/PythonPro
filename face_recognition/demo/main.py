from pywebio.input import *
from pywebio.output import *

from demo.face_data_collect import Collection


class FaceTools:
    def __init__(self):
        self.put_title("人脸识别功能")

    def start(self):
        collect_info = input_group('第一步：采集人脸数据', [
            input('face_num', type=NUMBER, name='face_num', required=True, placeholder=10),
            actions('action', [
                {'label': '开始采集', 'value': 'start'}
            ], name='action', help_text='actions'),
        ])
        if collect_info['action'] == 'start':
            self.collect(collect_info['face_num'])

    def collect(self, num):
        self.put_text("正在打开电脑相机，请稍后>>>")
        collection = Collection(face_name='zyj', face_id=1000)
        self.put_text("开始获取摄像头数据...")
        collection.save_user_pictures(total_count=num)
        self.put_text('采集完成')

    @staticmethod
    def put_title(title):
        style(put_html('<h3>{}</h3>'.format(title)), 'text-align:center')

    @staticmethod
    def put_text(text):
        put_html('<p>{}</p>'.format(text))


if __name__ == '__main__':
    face = FaceTools()
    face.start()
