import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo import AppConfig


class AppElement:
    driver = webdriver

    def findElementId(self, element_id, timeout=3):
        try:
            wait = WebDriverWait(self.driver, timeout)
            # element = wait.until(expected_conditions.visibility_of(By.ID, element_id))
            # 使用匿名函数
            element_id = AppConfig.element_path + element_id
            element = wait.until(lambda diver: self.driver.find_element_by_id(element_id))
            print("element.resourceId", element.get_attribute("resourceId"))
            return element
        except:
            print("element can't find")

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        print("......滑动开始......")
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
            self.waitTime(0.5)
        print("......滑动结束......")

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
            self.waitTime(0.5)

    def swipeLeft(self, element, t=500, n=1):
        x1 = element.size['width'] * 0.85
        y1 = element.size['height'] * 0.5
        x2 = element.size['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
            self.waitTime(0.5)

    def swipeRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, element, t=1000, n=1):
        x1 = element.size['width'] * 0.25
        y1 = element.size['height'] * 0.5
        x2 = element.size['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def methodTest(self):
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").text)
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").tag_name)
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("name"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("text"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("resourceId"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("className"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("checkable"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").get_attribute("clickable"))
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").size)
        print(self.driver.find_element_by_id("com.ennova.dreamlf:id/title_tv").location)

    def waitTime(self, time_span):
        time.sleep(time_span)
