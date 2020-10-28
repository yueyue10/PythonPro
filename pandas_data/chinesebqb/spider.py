import json
import random
import time

import requests
from lxml import etree

from chinesebqb.strutils import get_bqb_name
from poetry.utils import ComHeaders


class BqbBean(object):
    def __init__(self, bqb_img, bqb_name, images):
        self.bqb_img = bqb_img
        self.bqb_name = bqb_name
        self.images = images

    def __str__(self):
        return "".join(str(item) for item in (self.bqb_img, self.bqb_name, self.images))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Spider(object):

    def __init__(self):
        self.url = 'https://www.v2fy.com/p/000readme-chinesebqb/'

    def start(self):
        bqb_list = self.get_data_from_html(self.url)
        bqb_str = json.dumps(bqb_list, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        # print(bqb_str)
        self.save_json_in_json('表情包', bqb_str)

    def get_data_from_html(self, href):
        bgq_list = []
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        bqb_table = com_html.xpath('/html/body/main/article/div[1]/div/table[2]')[0]
        print(bqb_table)
        bqb_trs = bqb_table.xpath('./tbody/tr')
        for tr_index, bqb_tr in enumerate(bqb_trs):
            # if tr_index != 0: continue
            bqb_img = bqb_tr.xpath('./td[1]/img/@data-src')[0]
            # print(tr_img)
            tr_img_path = bqb_tr.xpath('./td[2]/a/@href')[0]
            bqb_name = get_bqb_name(tr_img_path)
            # print(bqb_name)
            imgList = self.get_bqb_from_html(tr_img_path)
            bqb_obj = BqbBean(bqb_img, bqb_name, imgList)
            print(bqb_obj)
            bgq_list.append(bqb_obj)
        # print(bgq_list)
        return bgq_list

    def get_bqb_from_html(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        img_h6s = com_html.xpath('//*[@class="post-inner thin "]/div[@class="entry-content"]/h6')
        img_list = []
        for img_h6 in img_h6s:
            img_path = img_h6.xpath('./a/@href')
            if not img_path: continue
            # print(img_path)
            img_path = img_path[0]
            img_list.append(img_path)
        return img_list

    # 获取html页码内容
    @staticmethod
    def get_html_text(url):
        time.sleep(random.uniform(0.5, 1.5))
        response = requests.get(url, headers=ComHeaders.pc_headers, timeout=(5, 60))
        if response.status_code == 200:
            content = response.text
        return content

    # 保存json数据到json文件中
    @staticmethod
    def save_json_in_json(name, jsonstr):
        with open('{}.json'.format(name), 'w') as f:
            f.write(jsonstr)


if __name__ == '__main__':
    spider = Spider()
    spider.start()
    # spider.get_bqb_from_html('https://www.v2fy.com/p/049CatEveryday_%E7%8C%AB%E5%92%AA%E6%97%A5%E5%B8%B8BQB/')
