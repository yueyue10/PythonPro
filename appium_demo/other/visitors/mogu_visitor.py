import json
import random
import time

import requests
# 请求头
from lxml import etree

from appium_demo.log import save_log
from appium_demo.other import json_data
from appium_demo.other.visitors.cookie.selenium_test import SeleniumClient

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


class MoGuRequest:
    '''使用《蘑菇代理》网址的动态ip，因为ip数量有限就不使用多线程'''

    # 百度
    bd_main_url_json = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E8%B5%B5%E5%9B%9B%E9%A5%B8%E9%A5%B9%E9%9D%A2&c=2589&src=0&wd2=&pn=0&sug=0&l=10&b=(12356672.188326357,4809792.545941422;12556426.244393302,4970411.113472803)&from=webmap&biz_forward={%22scaler%22:2,%22styles%22:%22pl%22}&sug_forward=&auth=KFE8H5I%40A9G04PDN00Ef%3D0MMK%40aCHd%3DWuxHLENxzzHxtDpnSCE%40%40By1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuBtR9KxXwUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuztexZFTHrwzDvqs2osGIRVOXI33LXFuyWWJL0IBggc1a&device_ratio=2&tn=B_NORMAL_MAP&nn=0&u_loc=12967743,4840033&ie=utf-8&t=1564712258807'
    bd_cai_url_json = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C&c=168&src=0&wd2=&pn=0&sug=0&l=19&b=(12524462.465,4915415;12524952.465,4915809)&from=webmap&biz_forward={%22scaler%22:2,%22styles%22:%22pl%22}&sug_forward=&auth=F468SdW9ODYCQDfxcDa7KLFxbaxGBPX3uxHLENxxNHEtBnlQADZZzy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuztQZ3wWvUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVtcvY1SGpuxztpFNEhjzgjyBKOHQBBODKximNNzCPyGllhIK&device_ratio=2&tn=B_NORMAL_MAP&nn=0&u_loc=12967743,4840033&ie=utf-8&t=1564711758575'
    # 博客
    blog_url = 'https://blog.csdn.net/a_yue10/article/details/97392747'
    # 代理网址
    easy_url = 'https://www.easy-mock.com/mock/5d3ea7aab080cd6e28ae9511/bigdata/ip_list'

    def __init__(self, count=5):
        self._proxy_list = []
        self._json_urls = [self.bd_cai_url_json, self.bd_main_url_json]
        self.mo_gu_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=b4c273db82cc4492a8790045e9b43c54&count=%d&expiryDate=0&format=1&newLine=2' % count

    def start(self, _type='easy'):
        if _type == 'mogu': self.get_mo_gu()
        if _type == 'easy': self.get_easy_json()
        self.save_data(_type)
        while self._proxy_list:
            for proxy in self._proxy_list:
                self.request_url(self.blog_url, proxy)
                for _json_url in self._json_urls:
                    self.get_easy_json(_json_url, proxy)
                selenium = SeleniumClient(proxy=proxy)
                selenium.go_url(SeleniumClient.gd_cai_url, SeleniumClient.gd_main_url)
        print('___________本轮请求已完成___________')

    # 请求蘑菇代理ip
    def get_mo_gu(self):
        # 存储代理的列表
        try:
            req = requests.get(self.mo_gu_url, headers=headers, timeout=5)
            print("json数据__%s__>>" % 'mogu', req.json())
            for ips in req.json().get("msg"):
                self._proxy_list.append("https" + '#' + ips.get("ip") + '#' + ips.get("port"))
        except Exception as e:
            print("json解析错误__%s__>>" % 'mogu', e)
        finally:
            self.wait_time(1)

    # 请求json数据
    def get_easy_json(self, _url=easy_url, proxy=''):
        headers['Accept'] = 'application/json; charset=utf-8'
        # 存储代理的列表
        proxy_meta = ''
        proxies = ''
        _url_type = ''
        if proxy: proxy_meta, proxies = self.get_proxy_meta(proxy)
        try:
            req = requests.get(_url, headers=headers, proxies=proxies, timeout=5)
            # print("json>>", req.text)
            if req.status_code == 200:
                if 'amap.com' in _url:
                    _url_type = '高德地图'
                    jsonObj = req.json()
                    if jsonObj.get("data"):
                        name = jsonObj.get('data').get("base").get("name")
                    elif jsonObj.get("poi_list"):
                        name = jsonObj.get("poi_list")[0].get("name")
                    print("json获取成功__%s__>>" % _url_type, proxy_meta, name)
                elif 'baidu' in _url:
                    _url_type = '百度地图'
                    name = req.json().get("result").get("what")
                    print("json获取成功__%s__>>" % _url_type, proxy_meta, name)
                else:  # easy-api
                    _url_type = 'easy-mock'
                    for ips in req.json().get("data"):
                        protocol = 'https'
                        if ips.get("Protocol"): protocol = ips.get("Protocol")
                        self._proxy_list.append(protocol + '#' + ips.get("IP") + '#' + str(ips.get("Port")))
            else:
                print("请求无响应：")
        except Exception as e:
            if _url_type:
                print("json解析错误__%s__>>" % _url_type, proxy_meta, e)
                save_log("json解析错误__%s__>>：" % _url_type, proxy_meta, e)
            else:
                dom = _url.split('//')[1].split('.com')[0]
                print("ip不可用__%s__>>" % dom, proxy_meta, e)
        finally:
            self.wait_time(2)

    # 默认请求博客
    def request_url(self, _url, proxy):
        proxy_meta = ''
        proxies = ''
        if proxy: proxy_meta, proxies = self.get_proxy_meta(proxy)
        try:
            s = requests.session()
            s.keep_alive = False
            req = requests.get(url=_url, headers=headers, proxies=proxies, timeout=5)
            req.encoding = 'utf-8'
            if req.status_code == 200:
                html = req.text
                com_html = etree.HTML(html)
                read_count = com_html.xpath('//span[@class="read-count"]')
                print(proxy_meta, read_count[0].text)
            else:
                print("请求无响应：")
        except Exception as e:
            self.remove_port(proxy)
            dom = _url.split('//')[1].split('.net')[0]
            print("ip不可用__%s__>>" % dom, proxy_meta, e)
            save_log("ip不可用__%s__>>" % dom, proxy_meta, e)
        finally:
            self.wait_time(2)

    # 保存json数据
    def save_data(self, _type):
        print("保存json文件到json.txt")
        data = []
        for proxy in self._proxy_list:
            split_proxy = proxy.split('#')
            proxy = {
                "IP": split_proxy[1],
                "Port": split_proxy[2],
                "Protocol": split_proxy[0]
            }
            data.append(proxy)
        json_data['data'] = data
        json_data['msg'] = '从%s爬取的代理ip数据' % _type
        data_json = json.dumps(json_data)
        f = open('json.txt', 'w')
        f.write(data_json)
        f.close()

    @staticmethod
    def get_proxy_meta(proxy):
        split_proxy = proxy.split('#')
        _proxy_http = split_proxy[0]
        _proxy_host = split_proxy[1]
        _proxy_port = split_proxy[2]
        proxy_meta = "%(http)s://%(host)s:%(port)s" % {
            "http": _proxy_http,
            "host": _proxy_host,
            "port": _proxy_port
        }
        proxies = {
            "http": proxy_meta,
            "https": proxy_meta,
        }
        return proxy_meta, proxies

    def remove_port(self, proxy):
        try:
            self._proxy_list.remove(proxy)
        except Exception as e:
            print('已经删除了', e)

    @staticmethod
    def wait_time(_time):
        time.sleep(_time)


def test_proxy_request(_type='mogu', count=2):
    mogu = MoGuRequest(count=count)
    mogu.start(_type=_type)


def test_json_request(_url=MoGuRequest.bd_main_url_json):
    mogu = MoGuRequest()
    mogu.get_easy_json(_url=_url)


def test_blog_request():
    mogu = MoGuRequest()
    mogu.request_url(_url=MoGuRequest.blog_url, proxy='')


if __name__ == '__main__':
    test_proxy_request(count=5)
    # test_proxy_request(_type='mogu')
    # test_blog_request()
    # test_json_request(_url=MoGuRequest.bd_main_url_json)
