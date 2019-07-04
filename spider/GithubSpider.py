#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 18:30
# @Author  : zhaoyj
# @Site    : 
# @File    : GithubSpider.py
# @Software: PyCharm

from lxml import etree

from utils import TimeUtils, HtmlUtils, StringUtils
from utils.ComHeaders import pc_headers
from configs.DbConfig import GithubTaskSql
from dbutils.MySql import MySql
from filters.eUtils import make_md5, hexists_md5_filter
from filters.LogUtils import Log

"""
 github项目爬取
"""


class GithubDataSpider(object):

    def __init__(self):
        self.md5github = "github:dataMd5"
        self.headers = pc_headers

    def parse_info(self, spider_url):
        st, html = self.get_list_page(spider_url)
        com_html = etree.HTML(html)
        link_els = com_html.xpath(
            '//div[@id="user-repositories-list"]//li[@class="col-12 d-flex width-full py-4 border-bottom public fork"]')
        link_els1 = com_html.xpath(
            '//div[@id="user-repositories-list"]//li[@class="col-12 d-flex width-full py-4 border-bottom public source"]')
        self.save_data(link_els)
        self.save_data(link_els1)

        TimeUtils.sleep_long()
        Log.info("github_ data spider successfully!")

    def save_data(self, link_els):
        for li in link_els:
            url_el_ = li.xpath("./div[1]/div[1]/h3/a/@href")
            data_url = "https://github.com" + "".join(url_el_)
            md5 = make_md5(data_url)
            if hexists_md5_filter(md5, self.md5github):
                Log.info("news info already exists!")
            else:
                title = li.xpath("./div[1]/div[1]/h3/a/text()")
                title = self.format_title(title[0])
                description = li.xpath("./div[1]/div[2]/p/text()")
                if description:
                    description = self.format_title(description[0])
                else:
                    description = ""
            info_val = [title, description, data_url]
            try:
                mysql = MySql()
                mysql.update(GithubTaskSql.github_insert, info_val)
                mysql.end(option='commit')
            except Exception as e:
                Log.info(e)
                Log.info('githubSpider mysql failed.')
                Log.info(info_val)
                continue

    def get_list_page(self, url):
        global content
        retry = 0
        st = 0  # st  1:fail 1:success
        while not st and (retry < 100):
            st, content = HtmlUtils.download_html(url, headers=self.headers)
        return st, content

    @staticmethod
    def format_title(info):
        if info:
            title = StringUtils.format_str_info(info)
        else:
            title = ""
        return title


if __name__ == '__main__':
    bu = GithubDataSpider()
    bu.parse_info('https://github.com/yueyue10?tab=repositories')
