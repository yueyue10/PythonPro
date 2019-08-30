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
           # 'Connection': 'close',
           # 'keep_alive ': 'False',
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

    def __init__(self, _page, _thread_num, _name=''):
        threading.Thread.__init__(self)
        self.page = _page
        self._name = _name
        self._thread_num = _thread_num
        self._proxy_list = []

    def run(self):
        threadLock.acquire()
        if self._name == 'mo_gu_url': self.get_mo_gu()
        if self._name == 'heng_xing_url': self.get_heng_xing()
        if self._name == 'easy_url': self.get_easy_json()
        self.save_data()
        threadLock.release()
        # 请求博客详情
        for proxy in self._proxy_list:
            split_proxy = proxy.split('#')
            self.http(blog_url, _proxyHttp=split_proxy[0], _proxyHost=split_proxy[1], _proxyPort=split_proxy[2])

    def get_mo_gu(self):
        # 存储代理的列表
        req = requests.get(dai_li_url.get('mo_gu_url'), headers=headers, timeout=5)
        print(time.time(), req.json())
        try:
            for ips in req.json().get("msg"):
                self._proxy_list.append("https" + '#' + ips.get("ip") + '#' + ips.get("port"))
                global_proxy_list.append("https" + '#' + ips.get("ip") + '#' + ips.get("port"))
        except Exception as e:
            print("json解析错误", e)
        finally:
            self.wait_time(5)

    def get_heng_xing(self):
        # 存储代理的列表
        req = requests.get(dai_li_url.get('heng_xing_url'), headers=headers, timeout=5)
        print(time.time(), req.text)
        try:
            for ips in req.json().get("data"):
                self._proxy_list.append("https" + '#' + ips.get("IP") + '#' + str(ips.get("Port")))
                global_proxy_list.append("https" + '#' + ips.get("IP") + '#' + str(ips.get("Port")))
        except Exception as e:
            print("json解析错误", e)
        finally:
            self.wait_time(5)

    def get_easy_json(self):
        headers['Accept'] = 'application/json; charset=utf-8'
        # 存储代理的列表
        req = requests.get(dai_li_url.get('easy_url'), headers=headers, timeout=5)
        print(time.time(), req.text)
        try:
            for ips in req.json().get("data"):
                protocol = 'https'
                if ips.get("Protocol"): protocol = ips.get("Protocol")
                self._proxy_list.append(protocol + '#' + ips.get("IP") + '#' + str(ips.get("Port")))
                global_proxy_list.append(protocol + '#' + ips.get("IP") + '#' + str(ips.get("Port")))
        except Exception as e:
            print("json解析错误", e)
        finally:
            self.wait_time(3)

    def wait_time(self, _time):
        time.sleep(_time)

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
            requests.adapters.DEFAULT_RETRIES = 3
            s = requests.session()
            s.keep_alive = False
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
            print("ip不可用：", proxy_meta)
            save_log("ip不可用：", proxy_meta, e)


def visit_blog(thread_num=20, _name="mo_gu_url"):
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
    '''使用《蘑菇代理》网址的动态ip，正常是收费的，因为新用户免费体验送了400条'''
    blog_url = 'https://blog.csdn.net/a_yue10/article/details/97392747'
    dai_li_url = {
        # 蘑菇代理
        'mo_gu_url': 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=5e9bf0cd2f574a93ad38600c67a805a5&count=10&expiryDate=0&format=1&newLine=2',
        # 恒星爬虫代理
        'heng_xing_url': 'http://120.79.197.226:8080/Index-generate_api_url.html?packid=1&fa=0&qty=10&port=1&format=json&ss=5&css=&pro=&city=&usertype=8',
        # easy_api
        'easy_url': 'https://www.easy-mock.com/mock/5d3ea7aab080cd6e28ae9511/bigdata/ip_list1',
    }
    threadLock = threading.Lock()
    global_proxy_list = []
    # visit_blog(thread_num=10, _name='mo_gu_url')
    # visit_blog(thread_num=10, _name='heng_xing_url')
    visit_blog(thread_num=1, _name='easy_url')
