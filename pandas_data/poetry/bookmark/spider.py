import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info
from poetry.utils import ComHeaders

DOMIN = 'http://www.shicimingju.com'
# 史书典籍地址
SHICI_BOOK_URL = DOMIN + '/book/'


# 史书典籍实体类
class BookMarkListBean(object):
    def __init__(self, title, bookmarks):
        self.title = title
        self.bookmarks = bookmarks

    def __str__(self):
        return "".join(str(item) for item in (self.title, self.bookmarks))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# 书籍标签实体类
class BookMarkBean(object):
    def __init__(self, name, desc, books):
        self.name = format_str_info(name)
        self.desc = format_str_info(desc)
        self.books = books

    def __str__(self):
        return "".join(str(item) for item in (self.name, self.desc, self.books))


class Spider(object):

    def __init__(self, url):
        self.url = url

    def start(self):
        bookmarkListBean = self.get_info_from_book_marks(self.url)
        bookmarklistBean_json = json.dumps(bookmarkListBean, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json(bookmarkListBean.title, bookmarklistBean_json)
        print(bookmarklistBean_json)

    # 获取史书典籍内容
    def get_info_from_book_marks(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        book_marks = com_html.xpath('//*[@id="main_left"]/div[@class="card booknark_card"]')
        bookmarkList = []
        for book_mark in book_marks:
            mark_a = book_mark.xpath('./h2/a/text()')
            mark_h2 = book_mark.xpath('./h2/text()')
            mark_ = mark_a[0] if len(mark_a) > 0 else mark_h2[0]
            des_text = book_mark.xpath('./div[@class="des"]/text()')
            des_ = des_text[0] if len(des_text) > 0 else ''
            books = book_mark.xpath('./ul/li/a/text()')
            bookmarkBean = BookMarkBean(mark_, des_, books)
            bookmarkList.append(bookmarkBean)
            # print(books)
        bookmarkListBean = BookMarkListBean("史书典籍", bookmarkList)
        return bookmarkListBean

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
    spider = Spider(SHICI_BOOK_URL)
    spider.start()
