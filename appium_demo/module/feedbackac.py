from selenium.webdriver.common.by import By

from appium_demo.base.activity import Activity
from appium_demo.module.pictureselectorac import PictureSelectorActivity


class FeedbackActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.inputContent()
        self.selectPicture()
        self.inputPhone()
        self.submitFeedBack()

    def inputContent(self):
        feedback_content = input("请输入建议反馈内容：")
        et_feedback_content = self.findElementId('et_feedback_content')
        et_feedback_content.send_keys(feedback_content)

    def selectPicture(self):
        self.driver.hide_keyboard()
        rv_select_photo = self.findElementId('rv_select_photo')
        rv_select_photo.find_elements(by=By.CLASS_NAME, value="android.widget.RelativeLayout")[0].click()
        pictureselectoractivity = PictureSelectorActivity()

    def inputPhone(self):
        phone_num = input("请输入手机号：")
        et_feedback_contact = self.findElementId('et_feedback_contact')
        et_feedback_contact.send_keys(phone_num)

    def submitFeedBack(self):
        self.findElementId('iv_right').click()
        self.waitTime(1)
