"""诗词分类数据"""
import json

import requests
from lxml import etree

DOMIN = 'http://www.shicimingju.com'
# 课本分类地址
SHICI_MARK_URL = DOMIN + '/shicimark'


class MarkObj(object):
    def __init__(self, image, title):
        self.image = image
        self.title = title

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Spider(object):
    def __init__(self, url):
        self.url = url

    def start(self):
        self.get_info_from_mark(self.url)

    # 获取分类古诗内容
    def get_info_from_mark(self, url):
        html = self.get_html_text(url)
        # print("网页的内容", html)
        com_html = etree.HTML(html)
        mark_card_div = com_html.xpath('//*[@id="main_left"]/div/div[@class="mark_card"]')
        # print("mark_card_div数据长度：", len(mark_card_div), mark_card_div)
        markobjs = []
        for index, mark in enumerate(mark_card_div):
            image = mark.xpath('.//a/img/@src')[0]
            href = mark.xpath('.//a/@href')[0]
            title = mark.xpath('.//h3/a/text()')[0]
            print("for循环", index, image, title)
            markobj = MarkObj(image, title)
            markobjs.append(markobj)
        # print("markobjs数据", markobjs)

        markobjs_json = json.dumps(markobjs, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        print("转换后的json文件", markobjs_json)
        self.save_json_in_json("诗词分类", markobjs_json)

    # 获取html页码内容
    @staticmethod
    def get_html_text(url, headers=None):
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
    spider = Spider(SHICI_MARK_URL)
    spider.start()
