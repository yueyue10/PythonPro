import random
import time

from selenium import webdriver

# 各种移动端
from hualian.utils import user_agent_mobile
from hualian.yzm.codeiden import baidu_2


class SeleniumClient:
    order_url = r'https://wechat-applet.beijing-hualian.com/maotai/maotai_88.html?token' \
                r'=ZjGY2cANhyi16PWu7Rn0pMwY78DOaSU0E1J1ZgxioOe=&channelId=14&moutaiPromoId=88&phone=18810126510'

    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.agent = random.choice(user_agent_mobile)
        # self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('lang=zh_CN.UTF-8')
        self.chromeOptions.add_argument('user-agent="%s"' % self.agent)
        self.browser = webdriver.Chrome(options=self.chromeOptions)

    def go_url(self, *_urls):
        # 清除浏览器cookies
        self.browser.delete_all_cookies()
        try:
            for url in _urls:
                self.browser.get(url)
                self.pre_order()
        except Exception as e:
            print("请求超时__>>", e)
        finally:
            self.quit()

    def pre_order(self):
        time.sleep(2)
        pre_order = self.browser.find_elements_by_xpath('/html/body/div[1]/div[4]')[0]
        print("预约", pre_order.text)
        pre_order.click()
        time.sleep(5)
        self.input_values()

    def input_values(self):
        input_store = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/input')[0]
        input_store.click()
        time.sleep(2)
        input_date = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/input')[0]
        input_date.click()
        time.sleep(2)
        add_span = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[5]/div/div[2]/span[2]')[0]
        for i in range(0, 29):
            add_span.click()
        code_img = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[9]/div/div[2]/img')[0]
        code_src = code_img.get_attribute("src")
        code_src = code_src.replace("data:image/png;base64,", "")
        print("src", code_src)
        code_str = baidu_2(code_src)
        code_input = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[9]/div/div[2]/input')[0]
        code_input.send_keys(code_str)
        take_order = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[11]')[0]
        take_order.click()
        time.sleep(5)

    def quit(self):
        if self.browser: self.browser.quit()


if __name__ == '__main__':
    selenium = SeleniumClient()
    selenium.go_url(SeleniumClient.order_url)
