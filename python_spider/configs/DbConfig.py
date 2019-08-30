#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/29 15:08
# @Author  : cjf
# @Site    : 数据库配置文件
# @File    : dbconfig.py
# @Software: PyCharm
"""
数据库配置
"""


# mysql配置
class MySqlConfig:
    # ################################ mysql测试数据库配置 ################################
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PWD = '123456'
    DB_NAME = 'spider_2019'
    DB_CHAR = 'utf8mb4'


class GithubTaskSql:
    github_insert = 'insert into github_data(title, description, news_url) VALUES (%s,%s,%s)'
