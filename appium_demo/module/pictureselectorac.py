from appium_demo.base.activity import Activity


class PictureSelectorActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.selectPic()

    def selectPic(self):
        ll_check = self.driver.find_elements_by_id('ll_check')
        if len(ll_check) >= 3:
            for check in ll_check[:3]:
                check.click()
        elif len(ll_check) > 1:
            ll_check[1].click()
        self.waitTime(1)
        self.findElementId('picture_tv_ok').click()
