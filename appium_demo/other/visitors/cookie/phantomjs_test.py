import base64
import random
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

user_agent_list_3 = [
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
]


class PhantomClient:
    gd_cai_url = 'https://surl.amap.com/4jViED1j7T9'  # 分享链接
    gd_main_url = 'https://surl.amap.com/4kS7TFI1Mj'

    def __init__(self, proxy=''):
        self._service_args = ''
        desired_cap = DesiredCapabilities.PHANTOMJS.copy()
        desired_cap['phantomjs.page.settings.userAgent'] = random.choice(user_agent_list_3)
        if proxy:
            self._service_args = self.get_proxy(proxy=proxy)
            self.driver = webdriver.PhantomJS(desired_capabilities=desired_cap, service_args=self._service_args)
        else:
            self.driver = webdriver.PhantomJS(desired_capabilities=desired_cap)

    def go_url(self, *_urls):
        # 清除浏览器cookies
        # self.driver.delete_all_cookies()
        try:
            for url in _urls:
                self.driver.get(url)
                self.print_content()
        except Exception as e:
            dom = self.gd_cai_url.split('//')[1].split('.com')[0]
            print("请求超时__%s__>>" % dom, self.proxy_meta, e)
        finally:
            self.quit()

    def print_content(self):
        time.sleep(1)
        span_text = self.driver.find_elements_by_xpath('//span[@class="name text-overflow"]')
        if span_text:
            print("html获取成功__高德地图__>>%s" % self.proxy_meta, span_text[0].text)

    def quit(self):
        if self.driver: self.driver.quit()

    @staticmethod
    def get_proxy(proxy):
        split_proxy = proxy.split('#')
        _proxy_http = split_proxy[0]
        _proxy_host = split_proxy[1]
        _proxy_port = split_proxy[2]
        proxy_meta = "%(http)s://%(host)s:%(port)s" % {
            "http": _proxy_http,
            "host": _proxy_host,
            "port": _proxy_port
        }
        __proxy = '--proxy=%s' % proxy_meta
        __proxy_type = '--proxy-type=%s' % _proxy_http
        service_args = [__proxy, __proxy_type, ]
        return service_args


if __name__ == '__main__':
    phantom = PhantomClient()
    phantom.go_url(PhantomClient.gd_cai_url, PhantomClient.gd_main_url)
