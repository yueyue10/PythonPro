# encoding:utf-8
import requests
import requests
import base64


def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'
    host = host.format("MUcPtsje9zlvXN7cItnbUC1H", "WRKeQ4rq85P9yyARMENFT6yeBuV3Mm4N")
    print(host)
    response = requests.get(host)
    if response:
        # print(response.json())
        jsonOjb=response.json()
        print(type(jsonOjb))
        access_token=jsonOjb.get("access_token")
        print(access_token)
        return access_token

def analysis():
    '''
    通用物体和场景识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open('1.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())


if __name__ == '__main__':
    analysis()
