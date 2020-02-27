class CovidBean(object):
    def __init__(self, nationdata, hubeirelated):
        self.nationdata = nationdata
        self.hubeirelated = hubeirelated

    class NationData(object):
        def __init__(self, newcase, nowcase, totalcase):
            self.newcase = newcase
            self.nowcase = nowcase
            self.totalcase = totalcase

        class NewCase(object):
            def __init__(self, new_confirm, new_suspect):
                self.new_confirm = new_confirm
                self.new_suspect = new_suspect

        class NowCase(object):
            def __init__(self, now_confirm, now_suspect, total_confirm):
                self.now_confirm = now_confirm
                self.now_suspect = now_suspect
                self.total_confirm = total_confirm

        class TotalCase(object):
            def __init__(self, total_cure, total_death):
                self.total_cure = total_cure
                self.total_death = total_death

    class HubeiRelated(object):
        def __init__(self, newcase, nowcase):
            self.newcase = newcase
            self.nowcase = nowcase

        class NewCase(object):
            def __init__(self, new_confirm_hb, new_confirm_nhb, new_confirm_nation):
                self.new_confirm_hb = new_confirm_hb
                self.new_confirm_nhb = new_confirm_nhb
                self.new_confirm_nation = new_confirm_nation

        class NowCase(object):
            def __init__(self, now_confirm_hb, now_confirm_nhb, now_confirm_nation):
                self.now_confirm_hb = now_confirm_hb
                self.now_confirm_nhb = now_confirm_nhb
                self.now_confirm_nation = now_confirm_nation