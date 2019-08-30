import json
import random
import threading
import time

import requests
# 请求头
from lxml import etree

from appium_demo.log import save_log
from appium_demo.other import json_data

user_agent_list = [
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
    'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
    'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'User-Agent': random.choice(user_agent_list),
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'keep_alive ': 'False',
           # 'Connection': 'close',
           }
# 完善的headers
target_headers = {'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Referer': 'http://www.xicidaili.com/nn/',
                  'Accept-Encoding': 'gzip, deflate, sdch',
                  'Accept-Language': 'zh-CN,zh;q=0.8',
                  }


class RequestRobot(threading.Thread):

    def __init__(self, _page, _thread_num, _name="xici"):
        threading.Thread.__init__(self)
        self.page = _page
        self._name = _name
        self._thread_num = _thread_num
        self._proxy_list = []

    def run(self):
        threadLock.acquire()
        print(time.time(), threading.currentThread().getName(), "______________获取代理列表______________", self.page)
        if self._name == 'xicidaili': self.get_proxy_xici()
        if self._name == 'kuaidaili': self.get_proxy_kuai_daili()
        self.save_data()
        threadLock.release()
        # 请求博客详情
        for proxy in self._proxy_list:
            split_proxy = proxy.split('#')
            self.http(blog_url, _proxyHttp=split_proxy[0], _proxyHost=split_proxy[1], _proxyPort=split_proxy[2])

    def get_proxy_xici(self):
        # requests的Session可以自动保持cookie,不需要自己维护cookie内容
        _session = requests.Session()
        # 西祠代理高匿IP地址
        target_url = dai_li_url.get('xicidaili') % self.page
        # get请求
        target_response = _session.get(url=target_url, headers=target_headers)
        # utf-8编码
        target_response.encoding = 'utf-8'
        # 获取网页信息
        target_html = target_response.text
        if target_response.status_code == 200:
            try:
                # 获取id为ip_list的table
                com_html = etree.HTML(target_html)
                ip_list_info = com_html.xpath('//table[@id="ip_list"]/tr')
                # 爬取每个代理信息
                for ip_info in ip_list_info[1:]:
                    ip = ip_info.xpath('./td[2]')[0].text
                    port = ip_info.xpath('./td[3]')[0].text
                    protocol = ip_info.xpath('./td[6]')[0].text.lower()
                    self._proxy_list.append(protocol + '#' + ip + '#' + port)
                    global_proxy_list.append(protocol + '#' + ip + '#' + port)
            except Exception as e:
                print(target_html, "\n解析出错", e)
            finally:
                time.sleep(2)
        else:
            print(target_url, '接口异常')

    def get_proxy_kuai_daili(self):
        _session = requests.Session()
        target_url = dai_li_url.get('kuaidaili') % self.page
        target_response = _session.get(url=target_url, headers=target_headers)
        target_response.encoding = 'utf-8'
        target_html = target_response.text
        if target_response.status_code == 200:
            try:
                com_html = etree.HTML(target_html)
                ip_list_info = com_html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
                # 爬取每个代理信息
                for ip_info in ip_list_info:
                    ip = ip_info.xpath('./td[1]')[0].text
                    port = ip_info.xpath('./td[2]')[0].text
                    protocol = ip_info.xpath('./td[4]')[0].text.lower()
                    self._proxy_list.append(protocol + '#' + ip + '#' + port)
                    global_proxy_list.append(protocol + '#' + ip + '#' + port)
            except Exception as e:
                print(target_html, "\n解析出错", e)
            finally:
                time.sleep(2)
        else:
            print(target_url, '接口异常')

    def save_data(self):
        if self.page == self._thread_num:
            print("保存json文件到json.txt")
            data = []
            for proxy in global_proxy_list:
                split_proxy = proxy.split('#')
                proxy = {
                    "IP": split_proxy[1],
                    "Port": split_proxy[2],
                    "Protocol": split_proxy[0]
                }
                data.append(proxy)
            json_data['data'] = data
            json_data['msg'] = '从%s爬取的代理ip数据' % self._name
            data_json = json.dumps(json_data)
            f = open('json.txt', 'w')
            f.write(data_json)
            f.close()

    # 请求博客详情
    def http(self, _url, _proxyHttp, _proxyHost, _proxyPort):
        proxy_meta = "%(http)s://%(host)s:%(port)s" % {
            "http": _proxyHttp,
            "host": _proxyHost,
            "port": _proxyPort
        }
        proxies = {
            "http": proxy_meta,
            "https": proxy_meta,
        }
        try:
            # print(self.proxies)
            # requests.adapters.DEFAULT_RETRIES = 3
            req = requests.get(url=_url, headers=headers, proxies=proxies, timeout=5)
            req.encoding = 'utf-8'
            if req.status_code == 200:
                html = req.text
                com_html = etree.HTML(html)
                read_count = com_html.xpath('//span[@class="read-count"]')
                if read_count:  # 输出：阅读数
                    print(proxy_meta, read_count[0].text)
            else:
                print("请求无响应：")
        except Exception as e:
            print("ip不可用：", proxy_meta, e)
            save_log("ip不可用：", proxy_meta, e)
        finally:
            time.sleep(1)


def visit_blog(thread_num=20, _name='xicidaili'):
    threads = []
    for x in range(0, thread_num):
        threads.append(RequestRobot(_page=x + 1, _thread_num=thread_num, _name=_name))
    # 启动所有线程
    for t in threads:
        t.start()
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()


if __name__ == '__main__':
    '''使用西刺代理网址的动态ip，因为是免费的成功率很低'''
    blog_url = 'https://blog.csdn.net/a_yue10/article/details/97392747'
    dai_li_url = {
        # 西刺代理
        'xicidaili': 'https://www.xicidaili.com/nn/%d',
        # 快代理
        'kuaidaili': 'https://www.kuaidaili.com/free/inha/%d',
    }
    threadLock = threading.Lock()
    global_proxy_list = []
    # visit_blog(thread_num=10, _name='xicidaili')
    visit_blog(thread_num=1, _name='kuaidaili')
