import pandas as pd


def read_excel():
    data = pd.read_excel('resource/涠洲岛和大峡谷异同.xlsx')
    data = pd.read_excel('resource/涠洲岛拼团排期和问题点.xlsx')
    print(data)


def read_json():
    data = pd.read_json('resource/ips.json')
    print(data)


if __name__ == '__main__':
    read_excel()
