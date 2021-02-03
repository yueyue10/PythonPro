# encoding:utf-8
import requests
from pywebio.input import *
from pywebio.output import *


def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'
    host = host.format("MUcPtsje9zlvXN7cItnbUC1H", "WRKeQ4rq85P9yyARMENFT6yeBuV3Mm4N")
    print(host)
    response = requests.get(host)
    if response:
        # print(response.json())
        jsonOjb = response.json()
        print(type(jsonOjb))
        access_token = jsonOjb.get("access_token")
        print(access_token)
        return access_token


def analysis():
    '''
    通用物体和场景识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 方法一：二进制方式打开图片文件
    # f = open('1.jpg', 'rb')
    # img = base64.b64encode(f.read())

    # 方法二：使用[pywebio.input]获取文件
    with use_scope('title'):
        put_html('<h2 style="text-align:center">选择图片进行识别</h2>')
    img = file_upload("选择图片", accept="image/*")

    with use_scope('title', clear=True):
        put_html('<h2 style="text-align:center">识别报告</h2>')
        put_html('<h3>文件名：%s</h3>' % (img['filename']))
    img = img['dataurl']

    params = {"image": img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res_json = response.json()
        res_list = res_json['result']
        res_table = [['相似度', '类别', '关键字']]
        for item in res_list:
            item_list = [item['score'], item['root'], item['keyword']]
            res_table.append(item_list)
        print(res_table)
        # # 表格输出
        put_html('<br/><h4>识别结果：</h4>')
        put_table(res_table)


if __name__ == '__main__':
    analysis()
