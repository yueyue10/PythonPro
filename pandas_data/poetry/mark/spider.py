import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info
from poetry.utils import ComHeaders

DOMIN = 'http://www.shicimingju.com'
# 课本分类地址
SHICI_MARK_URL = DOMIN + '/shicimark'


# 分类古诗实体类
class MarkPoetry(object):
    def __init__(self, title, image, time, author, poetrys):
        self.title = title
        self.image = image
        self.time = time
        self.author = author
        self.poetrys = poetrys

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.image, self.time, self.author, self.poetrys))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 古诗详情实体类
class Poetry(object):
    def __init__(self, title, index, time, author, content):
        self.title = format_str_info(title)
        self.index = format_str_info(index)
        self.time = format_str_info(time)
        self.author = format_str_info(author)
        self.content = content
        # print(title, time, author, content)

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.index, self.time, self.author, self.content))


class Spider(object):
    def __init__(self, url):
        self.url = url

    def start(self):
        self.get_info_from_mark(self.url)

    # 获取分类古诗内容
    def get_info_from_mark(self, url):
        html = self.get_html_text(url)
        com_html = etree.HTML(html)
        mark_card_div = com_html.xpath('//*[@id="main_left"]/div/div[@class="mark_card"]')
        for index, mark in enumerate(mark_card_div):
            image = mark.xpath('.//a/img/@src')[0]
            href = mark.xpath('.//a/@href')[0]
            title = mark.xpath('.//h3/a/text()')[0]
            # 保存
            gradepoetry = self.get_detail_from_mark(title, image, href)
            gradepoetry_json = json.dumps(gradepoetry, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
            self.save_json_in_json("markPoetrys", gradepoetry_json)
            print(gradepoetry_json)

    # 获取古诗详情内容
    def get_detail_from_mark(self, title, image, href):
        html_detail = self.get_html_text(DOMIN + href)
        com_html = etree.HTML(html_detail)
        # 第一个div
        mark_title = com_html.xpath('//*[@id="main_left"]/div/h1/text()')
        time = com_html.xpath('//*[@id="main_left"]/div/div[@class="filter-container"]/a/text()')
        author = com_html.xpath('//*[@id="main_left"]/div/div[@class="filter-container filter-hide"]/a/text()')
        # print(mark_title, time, author)
        # 第一页的数据
        poetrys_one_page = self.get_div_info_from_html(com_html)
        # id为list_nav的div(页码标签控件)
        navis = com_html.xpath('//*[@id="main_left"]/div[@id="list_nav"]/div[@id="list_nav_part"]/a')
        len_navis = len(navis)
        # 之后页面的数据
        poetrys_next_page = []
        if len_navis > 0:  # 按照它的逻辑，只要大于0即肯定大于3
            navis.pop(len_navis - 1)
            navis.pop(0)
            for navi in navis:
                next_page_href = navi.xpath('@href')[0]
                poetrys = self.get_detail_from_mark_next_page(next_page_href)
                poetrys_next_page += poetrys
        poetrys_one_page = poetrys_one_page + poetrys_next_page
        markPoetry = MarkPoetry(title, image, time, author, poetrys_one_page)
        return markPoetry

    # 获取下一页的数据
    def get_detail_from_mark_next_page(self, href):
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
        shici_card = html.xpath('//*[@id="main_left"]/div[@class="card shici_card"]/div')
        # 第N页的数据解析
        for shici in shici_card:
            if len(shici.xpath('@style')) > 0:
                pass
            else:
                # 左边布局信息
                left_info = shici.xpath('./div[@class="list_num_info"]/text()')
                left_infos = format_str_list(left_info)
                # print(format_str_list(left_info))
                # 右边布局信息
                right_info = shici.xpath('./div[@class="shici_list_main"]')[0]
                title = right_info.xpath('./h3/a/text()')[0]
                shici_content = right_info.xpath('./div[@class="shici_content"]/text()')
                shici_content_hide = right_info.xpath('./div[@class="shici_content"]/div/text()')
                if shici_content_hide:
                    shici_content = shici_content + shici_content_hide
                # print(format_str_list(shici_content))
                index = left_infos[0] if len(left_infos) > 0 else 0
                time = left_infos[1] if len(left_infos) > 1 else 'null'
                author = left_infos[2] if len(left_infos) > 2 else 'null'
                poetry = Poetry(title, index, time, author, format_str_list(shici_content))
                poetrys.append(poetry)
        return poetrys

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
        with open('{}.json'.format(name), 'a') as f:
            # json.dump(jsonstr, f, ensure_ascii=False)
            f.write(jsonstr)


if __name__ == '__main__':
    spider = Spider(SHICI_MARK_URL)
    spider.start()
