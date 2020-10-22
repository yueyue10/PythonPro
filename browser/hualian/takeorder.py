import random
import time

from selenium import webdriver

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
        self.browser.implicitly_wait(10)  # seconds

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
        pre_order = self.browser.find_elements_by_xpath('/html/body/div[1]/div[4]')
        pre_order = pre_order[0]
        print("预约文本", pre_order.text)
        # 预约是否可以点击
        while pre_order.text != "预约抢购":
            time.sleep(1)
            # self.hint_dialog()
            print("预约文本", pre_order.text)
        pre_order.click()
        # 弹窗是否显示
        dialog_show = False
        while not dialog_show:
            time.sleep(1)
            dialog_show = self.input_dialog()
        self.input_store()
        self.input_date()
        self.input_number()
        self.input_yzm()
        self.confirm_take_order()
        time.sleep(30)

    def hint_dialog(self):
        try:
            hint_dialog = self.browser.find_element_by_xpath('/html/body/div[4]')
            print("hint_dialog", hint_dialog)
            confirm_btn = self.browser.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]')
            confirm_btn1 = self.browser.find_element_by_xpath('/html/body/div[4]/div[3]/a')
            confirm_btn.click()
            confirm_btn1.click()
        except Exception as ec:
            print("hint_dialog", "没显示")

    # 判断弹窗是否出现
    def input_dialog(self):
        input_dialog = self.browser.find_element_by_xpath('/html/body/div[2]')
        # print(type(input_dialog))
        # if not isinstance(input_dialog, list):
        #     return False
        dialog_style = input_dialog.get_attribute("style")
        print("dialog_style", dialog_style)
        if not dialog_style:
            return False
        return True

    def input_store(self):
        input_store = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/input')[0]
        input_store.click()
        confirm_store = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a')
        confirm_store.click()
        # time.sleep(2)

    def input_date(self):
        input_date = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/input')[0]
        input_date.click()
        confirm_date = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a')
        confirm_date.click()
        # time.sleep(2)

    def input_number(self):
        add_span = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[5]/div/div[2]/span[2]')[0]
        for i in range(0, 29):
            add_span.click()

    def input_yzm(self):
        code_img = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[9]/div/div[2]/img')[0]
        code_src = code_img.get_attribute("src")
        code_src = code_src.replace("data:image/png;base64,", "")
        print("src", code_src)
        code_str = baidu_2(code_src)
        code_input = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[9]/div/div[2]/input')[0]
        code_input.send_keys(code_str)

    def confirm_take_order(self):
        take_order = self.browser.find_elements_by_xpath('/html/body/div[2]/div[1]/div[3]/div[11]')[0]
        take_order.click()

    def quit(self):
        if self.browser: self.browser.quit()


if __name__ == '__main__':
    selenium = SeleniumClient()
    selenium.go_url(SeleniumClient.order_url)
