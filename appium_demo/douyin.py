"""
获取抖音APP个人收藏内容的工具
"""
from base.appelement import AppElement
from module_douyin.mainac import MainActivity
from service import multi_appium, douyin_appium, AppConfig


class App(AppElement):
    # APP 里面的参数
    isLogin = False

    def __init__(self):
        print("正在打开APP...")

    def test(self):
        mainAc = MainActivity()
        mainAc.mine_test()
        # mainAc.mineTest()


# print("环境变量检查:", os.environ)
# print("ANDROID_HOME:", os.environ.get('ANDROID_HOME'))

if __name__ == "__main__":
    # 通过下面这种方式启动Android模拟器会出现一个启动窗口。可以在android_avd里面单独开启。
    # android_avd.start_avd(start_style='exe')
    AppConfig.element_path = 'com.ss.android.ugc.aweme:id/'
    douyin_appium.start_service()
    douyin_appium.con_device()
    app = App()
    app.test()
