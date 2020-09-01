import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info
from poetry.utils import ComHeaders

Color_Url = 'https://www.sojson.com/web/cj.html'


# 颜色集合实体类
class ColorListBean(object):
    def __init__(self, title, colorBeans):
        self.title = title
        self.colorBeans = colorBeans

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.colorBeans))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 颜色实体类
class ColorBean(object):
    def __init__(self, name, value):
        self.name = format_str_info(name)
        self.value = format_str_info(value)


class Spider(object):

    def __init__(self, url):
        self.url = url

    def start(self):
        colorListBean = self.get_info_from_colors(self.url)
        colorListBean_json = json.dumps(colorListBean, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json(colorListBean.title, colorListBean_json)
        print(colorListBean_json)

    # 获取颜色数据
    def get_info_from_colors(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        chinaColor = com_html.xpath('//*[@id="chinacolor"]/ul')
        colorList = []
        for index, colorUl in enumerate(chinaColor):
            colorLi = colorUl.xpath('./li')
            for colorItem in colorLi:
                colorName = colorItem.xpath('./a/text()')[0]
                colorValue = colorItem.xpath('./a/span/text()')[0]
                print(colorName, colorValue)
                colorBean = ColorBean(colorName, colorValue)
                colorList.append(colorBean)
        colorListBean = ColorListBean("中国传统色彩", colorList)
        return colorListBean

    # 获取html页码内容
    @staticmethod
    def get_html_text(url, headers=None):
        time.sleep(random.uniform(0.5, 1.5))
        response = requests.get(url, headers=ComHeaders.pc_headers, timeout=(5, 60))
        if response.status_code == 200:
            content = response.text
        return content

    # 保存json数据到json文件中
    @staticmethod
    def save_json_in_json(name, jsonstr):
        with open('{}.json'.format(name), 'w') as f:
            # json.dump(jsonstr, f, ensure_ascii=False)
            f.write(jsonstr)


if __name__ == '__main__':
    spider = Spider(Color_Url)
    spider.start()
