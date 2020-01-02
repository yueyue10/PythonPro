import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info

DOMIN = 'http://www.shicimingju.com'
# 作者合称地址
SHICI_HECHENG_URL = DOMIN + '/hecheng/index.html'


# 作者合称实体类
class AuthorHeCheng(object):
    def __init__(self, title, hechengs):
        self.title = title
        self.hechengs = hechengs

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.hechengs))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 合称实体类
class HeChengBean(object):
    def __init__(self, name, content):
        self.name = format_str_info(name)
        self.content = content

    def __str__(self):
        return "".join(str(item) for item in (self.name, self.content))


class Spider(object):

    def __init__(self, url):
        self.url = url

    def start(self):
        authorhecheng = self.get_info_from_hecheng(self.url)
        authorhecheng_json = json.dumps(authorhecheng, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json(authorhecheng.title, authorhecheng_json)
        print(authorhecheng_json)

    # 获取作者合称内容
    def get_info_from_hecheng(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        title = com_html.xpath('//*[@id="main_left"]/div[@class="card hc_card"]/h1/text()')[0]
        hecheng_divs = com_html.xpath('//*[@id="main_left"]/div[@class="card hc_card"]/div[@class="hecheng"]')
        hechengBeans = []
        for hecheng in hecheng_divs:
            name = hecheng.xpath('./h3/a/text()')[0]
            des_a = hecheng.xpath('./div[@class="des"]/a/text()')
            des_text = hecheng.xpath('./div[@class="des"]/text()')
            des_text = format_str_list(des_text)
            # print(des_a, des_text)
            hecheng_content = []
            for index, des in enumerate(des_a):
                des_item = {"des_a": des, "des_text": des_text[index]}
                hecheng_content.append(des_item)
                # print(des_item)
            # print(format_str_list(des))
            hechengBean = HeChengBean(name, hecheng_content)
            hechengBeans.append(hechengBean)
        authorhecheng = AuthorHeCheng(title, hechengBeans)
        return authorhecheng

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
    spider = Spider(SHICI_HECHENG_URL)
    spider.start()
