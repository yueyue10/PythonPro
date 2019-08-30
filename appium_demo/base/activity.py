from appium_demo.base.appelement import AppElement
from appium_demo.base.titlelayout import TitleLayout
from appium_demo.module import activity_list


class Activity(AppElement):
    def __init__(self, class_name):
        activity_class = activity_list.get(class_name, "NullActivityClass")
        self.driver.wait_activity(activity_class, 5)
        self.title = TitleLayout()
        # print("wait_activity=", activity_class)
        print("%s%s__%s%s" % ("________", class_name, self.title.getTitle(), "________"))

    def finish(self):
        self.title.finish()
