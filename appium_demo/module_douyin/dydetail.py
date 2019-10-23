from base.appelement import AppElement
from module_douyin import activity_list, share_str


class DetailActivity(AppElement):
    def __init__(self):
        activity_class = activity_list.get(self.__class__.__name__, "NullActivityClass")
        self.driver.wait_activity(activity_class, 5)
        self.share_process1()

    def share_process(self):
        dmt = self.findElementClass('android.support.v4.view.DmtViewPager$MyAccessibilityDelegate', position=-1)
        print("dmt长度" + len(dmt))
        shareBtn = self.driver.find_element_by_android_uiautomator("description(\"分享，按钮\")")
        if shareBtn:
            print("查找到shareBtn++++++++++++++++++++++++++++++++++++++++++")
            shareBtn.click()
            shareboard = ShareBoard()
        else:
            print("没有查找到shareBtn-------------------------------------------")

    def share_process1(self):
        self.waitTime(2)
        shareboard = ShareBoard()


class ShareBoard(AppElement):
    def __init__(self):
        self.waitTime(2)
        self.copy_process()

    def copy_process(self):
        ah = self.findElementId('ah')
        if ah: self.swipeRight(ah, 1000, 2)
        copyBtn = self.findElementTextWait('复制链接')
        if copyBtn: copyBtn.click()
        self.get_text()

    def get_text(self):
        ss = self.driver.getClipboardText()
        share_str.append(share_str)
