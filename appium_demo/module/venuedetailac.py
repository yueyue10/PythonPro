from appium_demo.base.activity import Activity


class VenueDetailActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.shareTest()
        self.findElementId("cancel_tv").click()
        self.title.finish()

    def shareTest(self):
        self.title.rightClick()
