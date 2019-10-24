import os
import threading

import requests
from selenium import webdriver

from other.tktask.test.test2 import FileSys, validate_title

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


class SeleniumClient:
    # 获取抖音去水印视频的工具网址
    target_url = 'http://3g.gljlw.com/diy/douyin.php'

    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.proxy_meta = ''
        self.agent = headers.get('User-Agent')
        self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('lang=zh_CN.UTF-8')
        self.chromeOptions.add_argument('user-agent="%s"' % self.agent)
        self.browser = webdriver.Chrome(options=self.chromeOptions)

    # 解析分享的抖音视频链接里面的视频下载地址
    def find_video_url(self, share_url):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            # 设置页面最大加载时间
            self.browser.set_page_load_timeout(10)
            self.browser.get(share_url)
            video = self.browser.find_element_by_xpath('//*[@id="theVideo"]')
            src_url = video.get_attribute('src')
            if src_url:
                print("视频地址>>>>>>>>>>>>>>>>>>>" + src_url)
                return src_url
            else:
                print("没有找到视频地址<<<<<<<<<<<<<" + share_url)
                return ''
        except Exception as e:
            print("解析出错", share_url, e)
        finally:
            self.quit()

    # 获取抖音去水印视频下载地址
    def get_no_sign_video_url(self, url):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            self.browser.get(self.target_url)
            input_e = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/input[1]')
            get_btn = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/input[2]')
            # 在输入框输入抖音视频分享地址
            input_e.send_keys(url)
            get_btn.click()
            # 获取成功，才能找到视频下载按钮控件
            download_e = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/a[1]')
            if download_e:
                down_url = download_e.get_attribute('href')
                print("视频地址>>>>>: " + down_url)
            self.browser.back()
            return down_url
        except Exception as e:
            print(e)
        finally:
            self.quit()

    def quit(self):
        if self.browser: self.browser.quit()


# 多线程下载文件类
class DownloadRobot(threading.Thread):
    m_save_path = r'E:\迅雷下载\抖音视频'
    m_save_name = r'%s.mp4'

    def __init__(self, _share_url, _video_name, _video_id, _down_type=1):
        threading.Thread.__init__(self)
        self._video_name = _video_name
        self._share_url = _share_url
        self._video_id = _video_id
        # 视频下载类型：1：抖音视频；2：去水印视频，使用第三方去水印工具网址处理，下载比较慢。
        self._down_type = _down_type

    def run(self):
        selenium_client = SeleniumClient()
        if self._down_type == 1:
            down_url = selenium_client.find_video_url(self._share_url)
        else:
            down_url = selenium_client.get_no_sign_video_url(self._share_url)
        if down_url:
            file_name = self.m_save_name % validate_title(self._video_name)
            self.download_media(down_url, self.m_save_path, file_name)

    @staticmethod
    def download_media(media_url, _save_path, _file_name, break_process=False):
        try:
            _file_path = os.path.join(_save_path, _file_name)
            pre_content_length = 0
            # 循环接收视频数据
            while True:
                # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
                if os.path.exists(_file_path):
                    if break_process:
                        headers['Range'] = 'bytes=%d-' % os.path.getsize(_file_path)
                    else:  # 这里的逻辑是处理下载多个抖音视频第一个后面的视频下载后不能播放的bug
                        break
                res = requests.get(media_url, stream=True, headers=headers, timeout=5)
                content_length = int(res.headers['content-length'])
                # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
                if content_length < pre_content_length or (
                        os.path.exists(_file_path) and os.path.getsize(
                    _file_path) == content_length) or content_length == 0:
                    break
                pre_content_length = content_length
                # 写入收到的视频数据
                with open(_file_path, 'ab') as file:
                    file.write(res.content)
                    file.flush()
                    print('下载成功>>>>>%s: file size : %d   total size:%d' % (
                        _file_name, os.path.getsize(_file_path), content_length))
        except Exception as e:
            print(e)


# 预下载前准备下载资源等
class PreDownload(object):
    _video_source_path = 'data.json'
    # 视频分享地址模板{%s}需要替换为视频id
    # mid=675018722444209639,这个是通过抖音分享个人的视频和别人的视频对比后得到的。这里如果是个人的视频统一用个人的mid，如果是他人的统一用一个他人的mid即可。
    # mid测试过程可参考helper_txt文件夹下test.txt里面的几个地址对比
    _reg_video_url = r'https://www.iesdouyin.com/share/video/%s/?region=CN&mid=675018722444209639&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme'

    # 开始资源预准备和下载
    def start(self, thread_num=20):
        video_data = self.get_video_list()
        # 这里偷懒处理了，正确应该是取一个向上取整的方法
        # 将视频list按照每组thread_num个进行分组，video_group_count 即视频的组数
        video_group_count = int(len(video_data) / thread_num) + 1
        # print("视频总数", len(video_data))
        # print("每组的个数", len(video_data) / thread_num)
        # print("视频的组数", int(len(video_data) / thread_num) + 1)
        # 将视频分组后的video_data都放到video_group_data里面组成一个二维list
        video_group_data = []
        # 根据视频总共的组数 video_group_count 将 video_data 进行分组并添加到 video_group_data 中
        for x in range(0, video_group_count):
            start = thread_num * x + 1
            end = thread_num * x + thread_num
            # print(start, end)
            # print(thread_data)
            x_thread_video_data = video_data[start:end]
            video_group_data.append(x_thread_video_data)
        # print("长度",len(video_group_data))
        for index, group_item_data in enumerate(video_group_data):
            print(group_item_data)
            print("\n=============================开始第%s个线程=============================" % str(index))
            # 将每组的视频数据放到线程里面进行下载
            self.start_download_thread(group_item_data)

    # 开启线程下载视频，线程数即传入的视频数
    def start_download_thread(self, _group_item_data):
        threads = []
        for y in range(0, len(_group_item_data)):
            video_name = _group_item_data[y][0]
            video_id = _group_item_data[y][1]
            video_url = self._reg_video_url % video_id
            file_sys = FileSys()
            con = file_sys.contain_file(video_name)
            if not con:  # 如果文件名不存在
                con1 = file_sys.contain_file(validate_title(video_name))
                if not con1:  # 如果格式化的文件名也不存在
                    # 创建DownloadRobot线程，添加到线程池threads里面
                    threads.append(DownloadRobot(video_url, video_name, video_id))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    # 从data.json中获取视频数据集合
    def get_video_list(self):
        video_list = []
        str_list = self.cut_str_to_list()
        for str_item in str_list:
            # 将字符串转成list
            video_item_list = eval(str_item)
            # print(video_item)
            video_list.append(video_item_list)
        # print(video_list)
        return video_list

    # 将data.json中的字符串分割成字符串集合
    def cut_str_to_list(self):
        # 保存字符串分割后得到的字符串集合
        str_list = []
        with open(self._video_source_path, 'r', encoding='utf-8') as f:
            data = f.read()
        # print(type(data))
        # 读取字符串第二位到最倒数第二位的中间的值
        cut_data = data[1:][:-1]
        # print(cut_data)
        cut_data = cut_data.replace('\n', '')
        # 根据data.json里面的格式使用下面的字符串进行分割得到视频信息的list
        cut_data = cut_data.split(',  [')
        for index, cut in enumerate(cut_data):
            # 将从第二项之后的数据缺少的‘[’补全
            if index != 0:
                cut = '[' + cut
            str_list.append(cut)
            # print(cut, index)
        return str_list


if __name__ == '__main__':
    pre_download = PreDownload()
    pre_download.start()
