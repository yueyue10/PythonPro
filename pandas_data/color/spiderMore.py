import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info
from poetry.utils import ComHeaders

Color_Url = 'https://webgradients.com/'


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
    def __init__(self, name, colorFrom, colorTo, colorText):
        self.name = format_str_info(name)
        if colorFrom:
            self.colorValue = colorFrom + "→" + colorTo
        else:
            self.colorValue = 'Many colors'
        self.colorText = colorText


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
        contentColor = com_html.xpath('//*[@class="index_page__content_section"]/div')
        colorList = []
        for index, colorDiv in enumerate(contentColor):
            colorCard = colorDiv.xpath('./div')
            for colorItem in colorCard:
                colorName = colorItem.xpath('./span[@class="gradient__title"]/text()')[0]
                colorValues = colorItem.xpath('./div[@class="gradient__colors_box"]/span/text()')
                colorText = colorItem.xpath('./button/@data-clipboard-text')
                colorFrom = ''
                colorTo = ''
                if colorValues:
                    colorFrom = colorValues[0]
                    colorTo = colorValues[2]
                colorBean = ColorBean(colorName, colorFrom, colorTo, colorText)
                colorList.append(colorBean)
        colorListBean = ColorListBean("webgradients", colorList)
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
