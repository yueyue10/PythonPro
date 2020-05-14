#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/29 15:53
# @Author  : cjf
# @Site    : 随机配置User-Agent
# @File    : ComHeaders.py
# @Software: PyCharm
import random
import time

from poetry.utils import UserAgents

mobile_headers = {
    'User-Agent': random.choice(UserAgents.mobile_agents),
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}

now_time = int(time.time())

pc_headers = {
    'User-Agent': random.choice(UserAgents.pc_agents),
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
