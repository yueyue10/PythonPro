from appium_demo import AppConfig
from appium_demo.base.activity import Activity


class LoginActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)

    def login(self):
        self.getYzm(AppConfig.phone_num)
        self.loginByYzm()

    def getYzm(self, phone_num):
        et_phone = self.findElementId('et_phone')
        et_phone.send_keys(phone_num)
        self.findElementId('time_code').click()

    def loginByYzm(self):
        yzm = input("请输入验证码:")
        et_code = self.findElementId('et_code')
        et_code.send_keys(yzm)
        self.findElementId('tv_login').click()
