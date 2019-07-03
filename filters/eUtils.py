#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/29 17:01
# @Author  : cjf
# @Site    : MD5
# @File    : eUtils.py
# @Software: PyCharm
import hashlib


def make_md5(data):
    tmp = hashlib.md5()
    tmp.update(data.encode("utf8"))
    fmd5 = tmp.hexdigest()
    return fmd5


# hexists md5
def hexists_md5_filter(vmd5, vmd_name):
    # video_hash = RedisCache(vmd_name)
    # if video_hash.hexists(vmd5):
    #     return 1
    # else:
    #     return 0
    return 0
