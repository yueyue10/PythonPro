import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info

DOMIN = 'http://www.shicimingju.com'
# 诗词排名地址
SHICI_PAIMING_URL = DOMIN + '/paiming?p=1'


# 古诗排名实体类
class PaiMingPoetry(object):
    def __init__(self, title, poetrys):
        self.title = title
        self.poetrys = poetrys

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.poetrys))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 古诗详情实体类
class Poetry(object):
    def __init__(self, title, index, time, author, shici_pic, content):
        self.title = format_str_info(title)
        self.index = format_str_info(index)
        self.time = format_str_info(time)
        self.author = format_str_info(author)
        self.pic = format_str_info(shici_pic)
        self.content = content
        # print(title, time, author, content)

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.index, self.time, self.author, self.pic, self.content))


class Spider(object):

    def __init__(self, url):
        self.url = url

    def start(self):
        paimingPoetry = self.get_info_from_paiming(self.url)
        paimingPoetry_json = json.dumps(paimingPoetry, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json(paimingPoetry.title, paimingPoetry_json)
        print(paimingPoetry_json)

    # 获取古诗排名内容
    def get_info_from_paiming(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        title = com_html.xpath('//*[@id="main_left"]/div[@class="card"]/h1/text()')[0]
        # 第一页的数据
        poetrys_one_page = self.get_div_info_from_html(com_html)
        # print("poetrys_one_page", poetrys_one_page)
        # id为list_nav的div(页码标签控件)
        navis = com_html.xpath('//*[@id="main_left"]/div[@id="list_nav"]/div[@id="list_nav_part"]/a')
        len_navis = len(navis)
        poetrys_next_page = []
        if len_navis > 0:  # 按照它的逻辑，只要大于0即肯定大于3
            navis.pop(len_navis - 1)
            navis.pop(len_navis - 2)
            navis.pop(0)
            for navi in navis:
                next_page_href = navi.xpath('@href')[0]
                poetrys = self.get_detail_from_paiming_next_page(next_page_href)
                poetrys_next_page += poetrys
        poetrys_one_page = poetrys_one_page + poetrys_next_page
        paimingPoetry = PaiMingPoetry(title, poetrys_one_page)
        return paimingPoetry

    # 获取下一页的数据
    def get_detail_from_paiming_next_page(self, href):
        html_detail = self.get_html_text(DOMIN + href)
        com_html = etree.HTML(html_detail)
        poetrys = self.get_div_info_from_html(com_html)
        return poetrys

    # 获取html页面的数据
    @staticmethod
    def get_div_info_from_html(html):
        # 当前页面的诗词集合
        poetrys = []
        # id为card shici_card的div
        shici_card = html.xpath('//*[@id="main_left"]/div[@class="card shici_card"]')
        # 第N页的数据解析
        for shici in shici_card:
            # 左边布局信息
            left_info = shici.xpath('./div[@class="list_num_info"]')[0]
            # print(left_info)
            times = left_info.xpath('./text()')
            time = format_str_list(times)[0]
            index = left_info.xpath('./span/text()')[0]
            author = left_info.xpath('./a/text()')[0]
            # print(index, time, author)
            # print(shici)
            # print(format_str_list(left_info))
            # 右边布局信息
            right_info = shici.xpath('./div[@class="shici_list_main"]')[0]
            # print("right_info", right_info)
            title = right_info.xpath('./h3/a/text()')[0]
            shici_content = right_info.xpath('./div[@class="shici_content"]/text()')
            shici_content_hide = right_info.xpath('./div[@class="shici_content"]/div/text()')
            if shici_content_hide:
                shici_content = shici_content + shici_content_hide
            # print(format_str_list(shici_content))
            # 图片布局信息
            shici_pic_a = shici.xpath('./div[@class="shici_list_pic"]/a/img')
            shici_pic = ""
            if len(shici_pic_a) > 0:
                shici_pic = shici_pic_a[0].xpath('@src')[0].split("?")[0]
            # print(shici_pic)
            poetry = Poetry(title, index, time, author, shici_pic, format_str_list(shici_content))
            poetrys.append(poetry)
        return poetrys

    # 获取html页码内容
    @staticmethod
    def get_html_text(url, headers=None):
        time.sleep(random.uniform(0.5, 1.5))
        response = requests.get(url, headers=headers, timeout=(5, 60))
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
    spider = Spider(SHICI_PAIMING_URL)
    spider.start()
