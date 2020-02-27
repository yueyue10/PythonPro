import json

import numpy as np
import pandas as pd

from pandastt.resource.CovidBean import CaseNewConfirm, CaseNowConfirm, CovidBean


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


# 肺炎数据类
class CovidVirus(object):
    def __init__(self, excel_file, json_file):
        self.excel_file = excel_file
        self.json_file = json_file

    def save_excel_to_json(self):
        json_data = self.get_excel_data()
        json_str = json.dumps(json_data, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        print('json_data', json_data)
        print('json_str', json_str)
        self.save_json_str(self.json_file, json_str)

    def get_excel_data(self):
        data = pd.read_excel(self.excel_file)
        case_data = []
        for i in data.index.values:  # 获取行号的索引，并对其进行遍历：
            case_date = self.get_value(data, i, '日期', False)
            case_new_confirm = self.get_value(data, i, '新增确诊')
            new_confirm_hb = self.get_value(data, i, '新增确诊_湖北')
            new_confirm_nhb = self.get_value(data, i, '新增确诊_非湖北')
            now_confirm_hb = self.get_value(data, i, '现有确诊_湖北')
            now_confirm_nhb = self.get_value(data, i, '现有确诊_非湖北')
            caseNewConfirm = CaseNewConfirm(new_confirm_hb, new_confirm_nhb)
            caseNowConfirm = CaseNowConfirm(now_confirm_hb, now_confirm_nhb)
            # 其他属性
            case_new_suspect = self.get_value(data, i, '新增疑似')
            case_now_confirm = self.get_value(data, i, '现有确诊')
            case_now_suspect = self.get_value(data, i, '现有疑似')
            case_total_confirm = self.get_value(data, i, '累计确诊')
            num_cure_total = self.get_value(data, i, '累计治愈')
            num_death_total = self.get_value(data, i, '累计死亡')
            covidBean = CovidBean(case_date, case_new_confirm, caseNewConfirm,
                                  case_new_suspect, case_now_confirm, caseNowConfirm,
                                  case_now_suspect, case_total_confirm, num_cure_total,
                                  num_death_total)
            case_data.append(covidBean)
        return case_data

    @staticmethod
    def get_value(data, i, key, is_int=True):
        if is_int:
            return int(data.loc[i, key])
        return data.loc[i, key]

    # 保存json信息到文件中
    @staticmethod
    def save_json_str(file_name, json_str):
        with open('{}.json'.format(file_name), 'w') as f:
            f.write(json_str)


if __name__ == '__main__':
    excel_path = 'resource/肺炎疫情_new.xlsx'
    json_name = '肺炎疫情'
    cv = CovidVirus(excel_path, json_name)
    cv.save_excel_to_json()
