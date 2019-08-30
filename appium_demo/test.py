from appium_demo.base.appelement import AppElement
from appium_demo.module.mainac import MainActivity
from appium_demo.service import multi_appium, android_avd


class App(AppElement):
    # APP 里面的参数
    isLogin = False

    def __init__(self):
        print("正在打开APP...")

    def test(self):
        mainAc = MainActivity()
        mainAc.homeTest(vp_test=False, grid_test=True)
        # mainAc.mineTest()


# print("环境变量检查:", os.environ)
# print("ANDROID_HOME:", os.environ.get('ANDROID_HOME'))

if __name__ == "__main__":
    # 通过下面这种方式启动Android模拟器会出现一个启动窗口。可以在android_avd里面单独开启。
    # android_avd.start_avd(start_style='exe')
    multi_appium.start_service()
    multi_appium.con_device()
    app = App()
    app.test()
