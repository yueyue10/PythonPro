from appium_demo.base.activity import Activity
from appium_demo.module.loginac import LoginActivity
from appium_demo.module.newsdetailac import NewsDetailActivity


class NewsListActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.scrollTest()
        self.voteTest()
        self.itemClickTest()
        self.finish()

    def voteTest(self):
        self.findElementId('likes_layout').click()
        self.waitTime(1)
        tv_title = self.findElementId("tv_title").text
        if tv_title == '登录':
            loginactivity = LoginActivity()
            loginactivity.finish()

    def itemClickTest(self):
        self.findElementId('news_iv').click()
        newsdetailactivity = NewsDetailActivity()

    def scrollTest(self):
        self.swipeUp(n=5)
