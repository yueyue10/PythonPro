import json
import threading
import time

import requests
from lxml import etree

from appium_demo.log import save_log
from appium_demo.other import json_data
from appium_demo.other.visitors.visitors_in_thread_html import target_headers, headers


class KuiDaiLi:
    threadLock = threading.Lock()
    blog_url = 'https://blog.csdn.net/a_yue10/article/details/97392747'
    dai_li_url = {
        # 西刺代理
        'xicidaili': 'https://www.xicidaili.com/nn/%d',
        # 快代理
        'kuaidaili': 'https://www.kuaidaili.com/free/inha/%d',
    }
    global_proxy_list = []

    def __init__(self):
        pass

    def start(self):
        self.visit_blog(thread_num=1, _name='kuaidaili')

    def visit_blog(self, thread_num=20, _name='xicidaili'):
        threads = []
        for x in range(0, thread_num):
            threads.append(RequestRobot(_page=x + 1, _thread_num=thread_num, _name=_name))
        # 启动所有线程
        for t in threads:
            t.start()
        # 主线程中等待所有子线程退出
        for t in threads:
            t.join()


class RequestRobot(threading.Thread):

    def __init__(self, _page, _thread_num, _name="xici"):
        threading.Thread.__init__(self)
        self.page = _page
        self._name = _name
        self._thread_num = _thread_num
        self._proxy_list = []

    def run(self):
        KuiDaiLi.threadLock.acquire()
        print(time.time(), threading.currentThread().getName(), "______________获取代理列表______________", self.page)
        if self._name == 'xicidaili': self.get_proxy_xici()
        if self._name == 'kuaidaili': self.get_proxy_kuai_daili()
        self.save_data()
        KuiDaiLi.threadLock.release()
        # 请求博客详情
        for proxy in self._proxy_list:
            split_proxy = proxy.split('#')
            self.http(KuiDaiLi.blog_url, _proxyHttp=split_proxy[0], _proxyHost=split_proxy[1],
                      _proxyPort=split_proxy[2])

    def get_proxy_xici(self):
        # requests的Session可以自动保持cookie,不需要自己维护cookie内容
        _session = requests.Session()
        # 西祠代理高匿IP地址
        target_url = KuiDaiLi.dai_li_url.get('xicidaili') % self.page
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
                    KuiDaiLi.global_proxy_list.append(protocol + '#' + ip + '#' + port)
            except Exception as e:
                print(target_html, "\n解析出错", e)
            finally:
                time.sleep(2)
        else:
            print(target_url, '接口异常')

    def get_proxy_kuai_daili(self):
        _session = requests.Session()
        target_url = KuiDaiLi.dai_li_url.get('kuaidaili') % self.page
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
                    KuiDaiLi.global_proxy_list.append(protocol + '#' + ip + '#' + port)
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
            for proxy in KuiDaiLi.global_proxy_list:
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
            req = requests.get(url=_url, headers=headers, proxies=proxies, timeout=2)
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
        finally:
            time.sleep(1)
