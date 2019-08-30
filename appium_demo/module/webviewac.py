from appium_demo.base.activity import Activity
from appium_demo.base.titlelayout import TitleLayout


class WebViewActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.scrollTest()

    def scrollTest(self):
        title = TitleLayout()
        self.swipeUp(n=5)
        title.finish()
