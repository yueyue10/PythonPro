import json

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info

DIR = "grade"
DOMIN = 'http://www.shicimingju.com'
# 课本古诗地址
SHICI_TEXTBOOK_URL = DOMIN + '/cate?cate_id=4'


# 课本古诗实体类
class GradePoetry(object):
    def __init__(self, grade, image, poetrys):
        self.grade = grade
        self.image = image
        self.poetrys = poetrys

    def __str__(self):
        return "".join(str(item) for item in (self.grade, self.image, self.poetrys))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 古诗详情实体类
class Poetry(object):
    def __init__(self, title, time, author, content):
        self.title = format_str_info(title)
        self.time = format_str_info(time)
        self.author = format_str_info(author)
        self.content = content
        # print(title, time, author, content)

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.time, self.author, self.content))


class Spider(object):
    def __init__(self, url):
        self.url = url

    def start(self):
        self.get_info_from_cate4(self.url)

    # 获取课本古诗内容
    def get_info_from_cate4(self, url):
        html = self.get_html_text(url)
        com_html = etree.HTML(html)
        cate_card_div = com_html.xpath('//*[@id="main_left"]/div[@class="cate_card"]/div')
        for cate in cate_card_div:
            if len(cate.xpath('@class')) > 0:
                title = cate.xpath('.//h3/a[1]/text()')[0]
                href = cate.xpath('.//h3/a[1]/@href')[0]
                image = cate.xpath('.//a/img/@src')[0]
                # print("title", title)
                gradepoetry = self.get_detail_from_cate(title, image, href)
                gradepoetry_json = json.dumps(gradepoetry, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
                self.save_json_in_json(gradepoetry.grade, gradepoetry_json)
                print(gradepoetry_json)
            else:
                pass

    # 获取古诗详情内容
    def get_detail_from_cate(self, title, image, href):
        html_detail = self.get_html_text(DOMIN + href)
        com_html = etree.HTML(html_detail)
        grade = com_html.xpath('//*[@id="main_left"]/div/h1/text()')
        shici_list = com_html.xpath('//*[@id="main_left"]/div')
        poetrys = []
        for shici in shici_list:
            shici_div = shici.xpath('div')
            for shici_info in shici_div:
                if len(shici_info.xpath('@class')) > 0:
                    continue
                else:
                    left = shici_info.xpath('./div[@class="list_num_info"]/text()')
                    author = shici_info.xpath('./div[@class="list_num_info"]/a/text()')
                    # print(format_str_list(left), author)
                    shici_title = shici_info.xpath('./div[@class="shici_list_main"]/h3/a/text()')
                    shici_content = shici_info.xpath(
                        './div[@class="shici_list_main"]/div[@class="shici_content"]/text()')
                    shici_content_hide = shici_info.xpath(
                        './div[@class="shici_list_main"]/div[@class="shici_content"]/div/text()')
                    if len(shici_content_hide) > 0:
                        shici_content = shici_content + shici_content_hide
                    poetry = Poetry(shici_title[0], left[1], author[0], format_str_list(shici_content))
                    # print(poetry)
                    # print(format_str_list(shici_content), format_str_list(shici_content1))
                    # print(poetry)
                    poetrys.append(poetry)
        gradepoetry = GradePoetry(title, image, poetrys)
        # print(gradepoetry)
        return gradepoetry

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
        with open('{}/{}.json'.format(DIR, name), 'w') as f:
            # json.dump(jsonstr, f, ensure_ascii=False)
            f.write(jsonstr)


if __name__ == '__main__':
    spider = Spider(SHICI_TEXTBOOK_URL)
    spider.start()
