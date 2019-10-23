import os
import threading

import requests
from selenium import webdriver

from other.tktask import save_path
from other.tktask.down_test.downloader import Downloader
from other.tktask.test.test2 import FileSys, validate_title

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


class SeleniumClient:
    target_url = 'http://3g.gljlw.com/diy/douyin.php'

    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.proxy_meta = ''
        self.agent = headers.get('User-Agent')
        self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('lang=zh_CN.UTF-8')
        self.chromeOptions.add_argument('user-agent="%s"' % self.agent)
        self.browser = webdriver.Chrome(options=self.chromeOptions)

    def go_url(self, url, file_name):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            self.browser.get(self.target_url)
            input = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/input[1]')
            getBtn = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/input[2]')
            input.send_keys(url)
            getBtn.click()
            downLoad = self.browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/a[1]')
            if downLoad:
                downUrl = downLoad.get_attribute('href')
                print("视频地址>>>>>: " + downUrl)
                download_media(downUrl, file_name)
            self.browser.back()
        except Exception as e:
            print(e)
        finally:
            self.quit()

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

    def quit(self):
        if self.browser: self.browser.quit()


class DownloadRobot(threading.Thread):

    def __init__(self, _video_name, _video_id):
        threading.Thread.__init__(self)
        self._video_name = _video_name
        self._video_id = _video_id

    def run(self):
        seleniumclient = SeleniumClient()
        url = "https://www.iesdouyin.com/share/video/%s/?region=CN&mid=6750187224442096398&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme"
        # seleniumclient.go_url(url % self._video_id, self._video_name)
        src_url = seleniumclient.find_video_url(url % self._video_id)
        if src_url:
            download_media(src_url, self._video_name)


def download_media(url, file_name, break_process=False):
    try:
        file_name = validate_title(file_name) + ".mp4"
        file_path = os.path.join(save_path, file_name)
        pre_content_length = 0
        # 循环接收视频数据
        while True:
            # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
            if os.path.exists(file_path):
                if break_process:
                    headers['Range'] = 'bytes=%d-' % os.path.getsize(file_path)
                else:  # 这里的逻辑是处理下载多个抖音视频第一个后面的视频下载后不能播放的bug
                    break
            res = requests.get(url, stream=True, headers=headers, timeout=5)
            content_length = int(res.headers['content-length'])
            # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
            if content_length < pre_content_length or (
                    os.path.exists(file_path) and os.path.getsize(file_path) == content_length) or content_length == 0:
                break
            pre_content_length = content_length
            # 写入收到的视频数据
            with open(file_path, 'ab') as file:
                file.write(res.content)
                file.flush()
                print('下载成功>>>>>%s: file size : %d   total size:%d' % (
                    file_name, os.path.getsize(file_path), content_length))
    except Exception as e:
        print(e)


def download_thread(partd):
    threads = []
    for y in range(0, len(partd)):
        video_name = partd[y][0]
        video_id = partd[y][1]
        filesys = FileSys()
        con = filesys.contain_file(video_name)
        if not con:  # 如果文件名不存在
            con1 = filesys.contain_file(validate_title(video_name))
            if not con1:  # 格式化的文件名也不存在
                threads.append(DownloadRobot(video_name, video_id))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def download_new(partd):
    url = "https://www.iesdouyin.com/share/video/%s/?region=CN&mid=6750187224442096398&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme"
    for y in range(0, len(partd)):
        video_name = partd[y][0]
        video_id = partd[y][1]
        file_name = video_name + ".mp4"
        file_path = os.path.join(save_path, file_name)
        down = Downloader(url % video_id, 10, file_path)
        down.run()


def download_test(partd):
    url = "https://www.iesdouyin.com/share/video/%s/?region=CN&mid=6750187224442096398&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme"
    for y in range(0, len(partd)):
        video_name = partd[y][0]
        video_id = partd[y][1]
        seleniumclient = SeleniumClient()
        src_url = seleniumclient.find_video_url(url % video_id)
        download_media(src_url, video_name)


def get_data():
    str_list = []
    new_list = []
    with open('data.json', 'r', encoding='utf-8') as f:
        data = f.read()
    print(type(data))
    cut_data = data[1:][:-1]
    # print(cut_data)
    cut_data = cut_data.replace('\n', '').replace('(', '').replace(')', '')
    cut_data = cut_data.split(',  [')
    for index, cut in enumerate(cut_data):
        if index != 0:
            cut = '[' + cut
        str_list.append(cut)
        # print(cut, index)
    for ss in str_list:
        ss_list = eval(ss)
        # print(ss_list)
        new_list.append(ss_list)
    # print(new_list)
    return new_list


def down_files():
    cut_data = get_data()
    for ss_list in cut_data:
        video_name = ss_list[0]
        video_id = ss_list[1]
        print("name=" + video_name, "id=" + video_id)
        seleniumclient = SeleniumClient()
        url = "https://www.iesdouyin.com/share/video/%s/?region=CN&mid=6750187224442096398&u_code=17h81ha7f&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme"
        seleniumclient.go_url(url % video_id, video_name)


def go_download(thread_num=20):
    cut_data = get_data()
    part_count = int(len(cut_data) / thread_num) + 1
    part_data = []
    # print("长度", len(cut_data))
    # print("长度", len(cut_data) / thread_num)
    # print("长度", int(len(cut_data) / thread_num) + 1)
    for x in range(0, part_count):
        start = thread_num * x + 1
        end = thread_num * x + thread_num
        # print(start, end)
        # print(thread_data)
        thread_data = cut_data[start:end]
        part_data.append(thread_data)
    # print("长度",len(part_data))
    for index, partd in enumerate(part_data):
        print(partd)
        print("\n=============================开始第%s个线程=============================" % str(index))
        download_thread(partd)


if __name__ == '__main__':
    # download_test()
    # get_data()
    # down_files()
    go_download()
