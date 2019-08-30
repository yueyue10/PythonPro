from appium_demo.base.appelement import AppElement


class TitleLayout(AppElement):

    def __init__(self):
        self.title = self.findElementId('tv_title')
        self.back = self.findElementId('iv_left')
        self.iv_right = self.findElementId('iv_right')

    def finish(self):
        self.waitTime(1.5)
        if self.back: self.back.click()

    def getTitle(self):
        if self.title: return self.title.text

    def rightClick(self):
        if self.iv_right: self.iv_right.click()
