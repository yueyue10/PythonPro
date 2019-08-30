"""
和项目无关的测试
visitors_in_thread：在线程里面获取动态ip，然后始用代理ip请求csdn博客地址来刷浏览量
"""
print("other 模块初始化")
json_data = {'code': 0,
             'success': 'true',
             'msg': '从%s爬取的代理ip数据',
             'data': []
             }
