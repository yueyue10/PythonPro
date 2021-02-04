# encoding:utf-8
import time
from functools import partial

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


def analysis(img):
    """
    通用物体和场景识别
    """

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 方法一：二进制方式打开图片文件
    # f = open('1.jpg', 'rb')
    # img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    res_table = [['相似度', '类别', '关键字']]
    if response:
        res_json = response.json()
        res_list = res_json['result']
        for item in res_list:
            item_list = [item['score'], item['root'], item['keyword']]
            res_table.append(item_list)
        print(res_table)
    return res_table


def start():
    # 方法二：使用[pywebio.input]获取文件
    with use_scope('title', clear=True):
        put_html('<h2 style="text-align:center">选择图片进行识别</h2>')

    img = file_upload("选择图片", accept="image/*", placeholder="浏览文件", required=True)
    img_bs = img['dataurl']

    with use_scope('pre-layout'):
        put_row([None, put_html('<br/><h4>图片名称：%s</h4>' % (img['filename'])), None], size='auto auto auto')
        put_row([None, put_image(img_bs, width='200px'), None], size='auto 200px auto')
        with use_scope('pre-loading'):
            put_loading(shape='grow', color='primary')
            put_html("<div>识别中...<div>")
            table_res = analysis(img_bs)
            time.sleep(3)
            clear()
        clear()

    with use_scope('title', clear=True):
        put_html('<h2 style="text-align:center">识别报告</h2>')
        put_html('<h3>图片名称：%s</h3>' % (img['filename']))
        put_image(img_bs, width='200px', scope='title', )

        # 表格输出
        put_html('<br/><h4>识别结果：</h4>')
        put_table(table_res)
        confirm = actions('', ['返回', '关闭'], help_text='')
        if confirm == '返回':
            start()
        elif confirm == '关闭':
            pass


if __name__ == '__main__':
    start()
