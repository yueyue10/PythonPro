import json

import numpy as np
import pandas as pd


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
    def __init__(self, excel_file, json_file, column):
        self.excel_file = excel_file
        self.json_file = json_file
        self.column = column

    # TypeError: Object of type int64 is not JSON serializable
    # 遇到上面的问题，参考这里解决：https://blog.csdn.net/ztf312/article/details/88866335
    def save_excel_to_json(self):
        json_data = self.get_excel_data()
        json_str = json.dumps(json_data, ensure_ascii=False, cls=NpEncoder)
        print('\n\njson_data\n', json_data)
        print('\n\njson_str\n', json_str)
        self.save_json_str(self.json_file, json_str)

    def get_excel_data(self):
        data = pd.read_excel(self.excel_file)
        test_data = []
        for i in data.index.values:  # 获取行号的索引，并对其进行遍历：
            # 根据i来获取每一行指定的数据 并利用to_dict转成字典
            row_data = data.loc[i, self.column].to_dict()
            test_data.append(row_data)
        # print(test_data)
        return test_data

    # 保存json信息到文件中
    @staticmethod
    def save_json_str(file_name, json_str):
        with open('{}.json'.format(file_name), 'w', encoding='utf-8') as f:
            f.write(json_str)


if __name__ == '__main__':
    excel_path = 'resource/肺炎疫情_new.xlsx'
    json_name = '新增确诊'
    column = ['日期', '新增确诊', '新增确诊湖北', '新增疑似']
    cv = CovidVirus(excel_path, json_name, column)
    cv.save_excel_to_json()
