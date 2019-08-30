import json

from appium_demo.other import json_data


def json_test():
    # 将字典转化成JSON来发送
    data_json = json.dumps(json_data)
    print(data_json)


if __name__ == '__main__':
    json_test()
