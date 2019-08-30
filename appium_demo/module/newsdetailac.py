from appium_demo.base.activity import Activity


class NewsDetailActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.swipeUp(n=3)
        self.finish()
