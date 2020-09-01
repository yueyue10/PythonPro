import codecs
import json
import random
import time

import requests
from lxml import etree

from poetry.string_utils import format_str_list, format_str_info
from poetry.utils import ComHeaders

TOP250_Url = 'https://movie.douban.com/top250?start={}&filter='


# 电影实体类
class MovieBean(object):
    def __init__(self, title, image, score, comment, director, actor, mtime, area, mtype, index):
        self.title = format_str_info(title)
        self.image = format_str_info(image)
        self.score = format_str_info(score)
        self.comment = format_str_info(comment)
        self.director = format_str_info(director)
        self.actor = format_str_info(actor)
        self.mtime = format_str_info(mtime)
        self.area = format_str_info(area)
        self.mtype = format_str_info(mtype)
        self.index = format_str_info(index)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Spider(object):

    def __init__(self, url):
        self.url = url

    def start(self):
        movie_list = []
        for index, i in enumerate(range(10)):
            video_url = self.url.format(i * 25)
            print(index, video_url)
            movieList = self.get_info_from_movie(video_url)
            movie_list = movie_list + movieList
        print(movie_list)
        movieList_json = json.dumps(movie_list, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
        self.save_json_in_json("电影TOP250", movieList_json)
        # print(colorListBean_json)

    # 获取电影数据
    def get_info_from_movie(self, href):
        html_detail = self.get_html_text(href)
        com_html = etree.HTML(html_detail)
        movieLis = com_html.xpath('//*[@class="article"]/ol/li')
        movieList = []
        for movieItem in movieLis:
            image = movieItem.xpath('./div/div[@class="pic"]/a/img/@src')[0]
            index = movieItem.xpath('./div/div[@class="pic"]/em/text()')[0]
            title = movieItem.xpath('./div/div[@class="info"]/div[@class="hd"]/a/span/text()')[0]
            content_text = movieItem.xpath('./div/div[@class="info"]/div[@class="bd"]/p[1]/text()')
            # print(content_text)
            content1 = format_str_info(content_text[0]).split("   ")
            # print(content1)
            director = content1[0]
            actor = ''
            if len(content1) > 1:
                actor = content1[1]
            content2 = format_str_info(content_text[1]).split("/")
            # print(content2)
            mtime = content2[0]
            area = content2[1]
            mtype = content2[2]
            # print(mtime, area, mtype)
            score = movieItem.xpath('./div/div[@class="info"]/div[@class="bd"]/div/span[@class="rating_num"]/text()')[0]
            comment = movieItem.xpath('./div/div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()')
            if comment:
                comment = comment[0]
            # print(desc)
            movieBean = MovieBean(title, image, score, comment, director, actor, mtime, area, mtype, index)
            movieList.append(movieBean)
        return movieList

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
        with codecs.open('{}.json'.format(name), 'w', 'utf-8') as f:
            f.write(jsonstr)


if __name__ == '__main__':
    spider = Spider(TOP250_Url)
    spider.start()
