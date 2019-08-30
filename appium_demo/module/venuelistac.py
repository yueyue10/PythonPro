from appium_demo.base.activity import Activity
from appium_demo.module.venuedetailac import VenueDetailActivity


class VenueListActivity(Activity):
    def __init__(self):
        Activity.__init__(self, self.__class__.__name__)
        self.scrollTest()
        self.toDetail()

    def scrollTest(self):
        vp_venue = self.findElementId("vp_venue")
        if vp_venue: self.swipeLeft(element=vp_venue, n=2)

    def toDetail(self):
        tv_to_detail = self.findElementId("tv_to_detail")
        tv_to_detail.click()
        detail = VenueDetailActivity()
        self.title.finish()
