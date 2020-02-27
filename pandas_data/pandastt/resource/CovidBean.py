import json


class CovidBean(object):
    def __init__(self, case_date, case_new_confirm, caseNewConfirm, case_new_suspect,
                 case_now_confirm, caseNowConfirm, case_now_suspect, case_total_confirm,
                 num_cure_total, num_death_total):
        self.case_date = case_date
        self.case_new_confirm = case_new_confirm
        self.caseNewConfirm = caseNewConfirm
        self.case_new_suspect = case_new_suspect
        self.case_now_confirm = case_now_confirm
        self.caseNowConfirm = caseNowConfirm
        self.case_now_suspect = case_now_suspect
        self.case_total_confirm = case_total_confirm
        self.num_cure_total = num_cure_total
        self.num_death_total = num_death_total

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class CaseNewConfirm(object):
    def __init__(self, new_confirm_hb, new_confirm_nhb):
        self.new_confirm_hb = new_confirm_hb
        self.new_confirm_nhb = new_confirm_nhb

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class CaseNowConfirm(object):
    def __init__(self, now_confirm_hb, now_confirm_nhb):
        self.now_confirm_hb = now_confirm_hb
        self.now_confirm_nhb = now_confirm_nhb

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
