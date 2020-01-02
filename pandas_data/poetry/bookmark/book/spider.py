import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info

DOMIN = 'http://www.shicimingju.com'
# 书籍目录地址
SHICI_BOOK_INFO_URL = DOMIN + '/book/sanguoyanyi.html'
SHICI_BOOK_INFO_URL = DOMIN + '/book/shuihuzhuan.html'
SHICI_BOOK_INFO_URL = DOMIN + '/book/xiyouji.html'
SHICI_BOOK_INFO_URL = DOMIN + '/book/hongloumeng.html'


# 分类古诗实体类
class BookBean(object):
    def __init__(self, name, image, year, author, desc, chapters):
        self.name = name
        self.image = image
        self.year = year
        self.author = author
        self.desc = desc
        self.chapters = chapters

    def __str__(self):
        return "".join(str(item) for item in (self.name, self.image, self.year, self.author, self.desc, self.chapters))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 古诗详情实体类
class ChapterBean(object):
    def __init__(self, title, paragraphs):
        self.title = format_str_info(title)
        self.paragraphs = paragraphs

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.paragraphs))


class Spider(object):
    def __init__(self, url):
        self.url = url

    def start(self):
        bookbean = self.get_info_from_book(self.url)
        bookbean_json = json.dumps(bookbean, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json(bookbean.name, bookbean_json)
        print(bookbean_json)

    # 获取书籍目录内容
    def get_info_from_book(self, url):
        html = self.get_html_text(url)
        com_html = etree.HTML(html)
        book_div = com_html.xpath('//*[@id="main_left"]/div[@class="card bookmark-list"]')[0]
        name = book_div.xpath('./h1/text()')[0]
        img = book_div.xpath('./div/img')[0].xpath('@src')[0]
        image = DOMIN + img
        year = book_div.xpath('./div/p')[0].xpath('./text()')[0]
        author = book_div.xpath('./div/p')[1].xpath('./text()')[0]
        desc = book_div.xpath('./div/p')[2].xpath('./text()')[0]
        # print(time, author,desc)
        chapters_text = book_div.xpath('./div[@class="book-mulu"]/ul/li/a/text()')
        chapters_href = book_div.xpath('./div[@class="book-mulu"]/ul/li/a/@href')
        # print(chapters_href)
        chapters = []
        for index, href in enumerate(chapters_href):
            chapterbean = self.get_book_chapter(href)
            chapters.append(chapterbean)
            print('{}-第{}章保存成功！'.format(name, index + 1))
        bookbean = BookBean(name, image, year, author, desc, chapters)
        return bookbean

    # 获取书籍详情内容
    def get_book_chapter(self, href):
        html_detail = self.get_html_text(DOMIN + href)
        com_html = etree.HTML(html_detail)
        chapter_div = com_html.xpath('//*[@id="main_left"]/div[@class="card bookmark-list"]')[0]
        title = chapter_div.xpath('./h1/text()')[0]
        # chapter_content-p标签里面的内容
        paragraphs_p = chapter_div.xpath('./div[@class="chapter_content"]/p/text()')
        paragraphs_p = format_str_list(paragraphs_p)
        # chapter_content里面的内容
        paragraphs_text = chapter_div.xpath('./div[@class="chapter_content"]/text()')
        paragraphs_text = format_str_list(paragraphs_text)
        paragraphs = paragraphs_p if len(paragraphs_p) > 0 else paragraphs_text
        chapterbean = ChapterBean(title, paragraphs)
        return chapterbean

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
    spider = Spider(SHICI_BOOK_INFO_URL)
    spider.start()
