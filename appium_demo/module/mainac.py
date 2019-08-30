from selenium.webdriver.common.by import By

from appium_demo.base.appelement import AppElement
from appium_demo.module import activity_list
from appium_demo.module.feedbackac import FeedbackActivity
from appium_demo.module.loginac import LoginActivity
from appium_demo.module.newslistac import NewsListActivity
from appium_demo.module.venuelistac import VenueListActivity
from appium_demo.module.webviewac import WebViewActivity


class MainActivity(AppElement):
    def __init__(self):
        print("________主页界面测试________")
        activity_class = activity_list.get(self.__class__.__name__, "NullActivityClass")
        self.driver.wait_activity(activity_class, 5)

    def homeTest(self, vp_test=True, grid_test=True):
        home_fragment = HomeFragment()
        if vp_test: home_fragment.viewPagerTest()
        if grid_test: home_fragment.gridClick()

    def mineTest(self):
        self.waitTime(1)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ImageView").click()
        user_name_tv = self.findElementId('user_name_tv').text
        if user_name_tv == '未登录':
            self.findElementId('user_icon_iv').click()
            loginactivity = LoginActivity()
            loginactivity.finish()
        else:
            pass


class HomeFragment(AppElement):
    def __init__(self):
        print("_______App首页UI测试_______")

    def viewPagerTest(self):
        viewPager = self.findElementId("viewPager")
        if viewPager:
            self.swipeLeft(element=viewPager, n=3)
            viewPager.click()
            webviewactivity = WebViewActivity()
        self.waitTime(1)

    def gridClick(self, module_num=-1):
        '''模块点击测试
        :param module_num: -1测试全部，0测试门票，1测试场馆，2测试资讯，3测试建议反馈
        :return:
        '''
        module_rv = self.findElementId("module_rv")
        if module_num == 0 or module_num == -1:
            # 门票预定点击
            module_rv.find_elements(by=By.CLASS_NAME, value="android.widget.LinearLayout")[0].click()
            self.waitTime(1)
        if module_num == 1 or module_num == -1:
            # 场馆介绍点击
            module_rv.find_elements(by=By.CLASS_NAME, value="android.widget.LinearLayout")[1].click()
            venuelistactivity = VenueListActivity()
            self.waitTime(1)
        if module_num == 2 or module_num == -1:
            # 活动资讯点击
            module_rv.find_elements(by=By.CLASS_NAME, value="android.widget.LinearLayout")[2].click()
            newslistactivity = NewsListActivity()
            self.waitTime(1)
        if module_num == 3 or module_num == -1:
            # 建议反馈点击
            module_rv.find_elements(by=By.CLASS_NAME, value="android.widget.LinearLayout")[3].click()
            feedbackactivity = FeedbackActivity()
