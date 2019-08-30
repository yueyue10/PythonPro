import json
import urllib
from urllib import request, parse

print('''---------------------urllib---------------------
''')


# urllib提供了一系列用于操作URL的功能。

# *********** Get ***********
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
# 例如，对豆瓣的一个URL https://api.douban.com/v2/book/2129650进行抓取，并返回响应：
def getEasyApi():
    with request.urlopen('https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/getUserInfo') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        data_str = data.decode('utf-8')
        print('Data:', data_str)
        print(type(data_str))
        assert json.loads(data_str)['object']['newsTitle'] == '让旅游多点文化味...'
        print('ok')


def getDobanMobileApi():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# *********** Post ***********
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
def postWeiboApi():
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# *********** Handler ***********
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
def postTest():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        print('Status:', f.status, f.reason)


# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象：
def fetch_data(url):
    return ''


# 测试
def fetch_data():
    with request.urlopen('https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest') as f:
        data = f.read()
        data_str = data.decode('utf-8')
        print(data)
        assert json.loads(data_str)['query']['results']['channel']['location']['city'] == 'Beijing'
        print('ok')
        return json.loads(data_str)


def test():
    # yueyue123zhao@163.com
    # getEasyApi()
    # getDobanMobileApi()
    # postWeiboApi()
    # postTest()
    fetch_data()


test()
