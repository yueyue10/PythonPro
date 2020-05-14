import time

from base.appelement import AppElement
from module_douyin import activity_list
from module_douyin.dydetail import DetailActivity
from utils.time_util import now_datetime


class MainActivity(AppElement):
    def __init__(self):
        activity_class = activity_list.get(self.__class__.__name__, "NullActivityClass")
        self.driver.wait_activity(activity_class, 5)
        print("________主页界面测试________")
        # self.elementTest()
        # vp = self.findElementClass("android.support.v4.view.ViewPager")
        # if vp: vp.click()

    def mine_test(self):
        self.waitTime(3)
        self.findElementText('酒店').click()
        time.sleep(2)
        print(self.driver.page_source)

        # 选择城市
        city_el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")
        city_el.click()
        time.sleep(3)
        cit_sea_el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
        cit_sea_el.send_keys("泰山")
        # os.system('adb shell ime set com.sohu.inputmethod.sogou.chuizi/.SogouIME')
        time.sleep(5)
        self.driver.press_keycode(66)  # 点回车
        time.sleep(2)

    def elementTest(self):
        e3z = self.findElementId('e3z')
        den = self.findElementId('den')
        if e3z:
            print(e3z.text)
        else:
            print("e3z没找到")
        if den:
            print(den.text)
        else:
            print("den没找到")
        try:
            sy = self.driver.find_element_by_android_uiautomator("text(\"首页\")")
            print(sy.text)
        except:
            print('首页没找到')
            pass


class MineFragment(AppElement):
    def __init__(self):
        print("________我的界面________")
        likeBtn = self.findElementTextWait('喜欢 1000')
        if likeBtn: likeBtn.click()
        print('点击喜欢按钮' + now_datetime())
        self.waitTime(3)
        self.likesClick()

    def likesClick(self):
        print('查找喜欢下面的列表' + now_datetime())
        ahsRv = self.findElementId("ahs")
        if ahsRv:
            frameLayout = self.findElementClass("android.widget.FrameLayout", position=-1, parent=ahsRv)
            frameLayout[0].click()
            detailActivity = DetailActivity()
