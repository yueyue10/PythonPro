import random
import time

from selenium import webdriver

# 各种移动端
from selenium.webdriver import ActionChains

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


class SeleniumClient:
    gd_cai_url = 'https://surl.amap.com/4jViED1j7T9'  # 分享链接
    gd_main_url = 'https://surl.amap.com/4kS7TFI1Mj'

    def __init__(self, proxy=''):
        self.chromeOptions = webdriver.ChromeOptions()
        self.proxy_meta = ''
        if proxy:
            self.proxy_meta = self.get_proxy(proxy=proxy)
            self.chromeOptions.add_argument('--proxy-server="%s"' % self.proxy_meta)
            # print('--proxy-server="%s"' % self.proxy_meta)
        self.agent = random.choice(user_agent_list_3)
        self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('lang=zh_CN.UTF-8')
        self.chromeOptions.add_argument('user-agent="%s"' % self.agent)
        self.browser = webdriver.Chrome(options=self.chromeOptions)

    def go_url(self, *_urls):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            for url in _urls:
                self.browser.get(url)
                self.print_content()
        except Exception as e:
            dom = self.gd_cai_url.split('//')[1].split('.com')[0]
            print("请求超时__%s__>>" % dom, self.proxy_meta, e)
        finally:
            self.quit()

    def move_slide(self):
        iframe = self.browser.find_element_by_xpath('//iframe')  # 找到“嵌套”的iframe
        self.browser.switch_to.frame(iframe)  # 切换到iframe
        btn_slide = self.browser.find_element_by_xpath('//span[@class="nc_iconfont btn_slide"]')

        action = ActionChains(self.browser)  # 实例化一个action对象
        action.click_and_hold(btn_slide).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        action.move_by_offset(256, 0).perform()  # 移动滑块
        time.sleep(3)

    def print_content(self):
        time.sleep(2)
        span_text = self.browser.find_elements_by_xpath('//span[@class="name text-overflow"]')
        # span_text = self.browser.find_elements_by_xpath('//h3[@class="poiname"]')
        if span_text:
            print("html获取成功__高德地图__>>%s" % self.proxy_meta, span_text[0].text)

    def quit(self):
        if self.browser: self.browser.quit()

    @staticmethod
    def get_proxy(proxy):
        split_proxy = proxy.split('#')
        _proxy_http = split_proxy[0]
        _proxy_host = split_proxy[1]
        _proxy_port = split_proxy[2]
        proxy_meta = "%(http)s=%(host)s:%(port)s" % {
            "http": _proxy_http,
            "host": _proxy_host,
            "port": _proxy_port
        }
        return proxy_meta


if __name__ == '__main__':
    selenium = SeleniumClient()
    selenium.go_url(SeleniumClient.gd_cai_url, SeleniumClient.gd_main_url)
