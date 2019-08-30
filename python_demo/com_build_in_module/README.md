# 常用内建模块
### 知识点总结

> * datetime

     1. datetime.now() # 获取当前datetime
        datetime.now()返回当前日期和时间，其类型是datetime。
     2. datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
        >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
        >>> print(dt)
        2015-04-19 12:20:00
     3. datetime转换为timestamp
        >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
        >>> dt.timestamp() # 把datetime转换为timestamp
        1429417200.0
        timestamp是一个浮点数。
     4. fromtimestamp()
        >>> t = 1429417200.0
        >>> print(datetime.fromtimestamp(t)) # 本地时间
        2015-04-19 12:20:00
        >>> print(datetime.utcfromtimestamp(t)) # UTC时间
        2015-04-19 04:20:00
        timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
     5. str转换为datetime
        >>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
        >>> print(cday)
        2015-06-01 18:19:59
     6. datetime转换为str
        >>> now = datetime.now()
        >>> print(now.strftime('%a, %b %d %H:%M'))
        Mon, May 05 16:28
     7. datetime加减
        now = datetime.now()
        now + timedelta(hours=10)
        now - timedelta(days=1)
        now + timedelta(days=2, hours=12)
     8. 时区转换
        astimezone()

> * collections

     1. namedtuple
        namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
        并可以用属性而不是索引来引用tuple的某个元素
        Point = namedtuple('Point', ['x', 'y'])
        Circle = namedtuple('Circle', ['x', 'y', 'r'])
     2. deque
        deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
        deque除了实现list的append()和pop()外，还支持appendleft()和popleft()
     3. defaultdict
        使用dict时，如果引用的Key不存在，返回一个默认值，就可以用defaultdict：
        >>> dd = defaultdict(lambda: 'N/A')
        >>> dd['key1'] = 'abc'
        >>> dd['key1'] # key1存在
        'abc'
        >>> dd['key2'] # key2不存在，返回默认值
        'N/A'
     4. OrderedDict
        使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
        如果要保持Key的顺序，可以用OrderedDict：
        >>> d = dict([('a', 1), ('b', 2), ('c', 3)])
        >>> d # dict的Key是无序的
        {'a': 1, 'c': 3, 'b': 2}
        >>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
        >>> od # OrderedDict的Key是有序的
        OrderedDict([('a', 1), ('b', 2), ('c', 3)])

        注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
     5. ChainMap
        ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
        ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
     6. Counter
        Counter是一个简单的计数器，例如，统计字符出现的个数：
        >>> c = Counter()
        >>> for ch in 'programming':
        ...     c[ch] = c[ch] + 1
        ...
        >>> c
        Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

> * base64

     1. Base64是一种用64个字符来表示任意二进制数据的方法。
        >>> base64.b64encode(b'binary\x00string')
        b'YmluYXJ5AHN0cmluZw=='
        >>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
        b'binary\x00string'
     2. 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
        所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
        >>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
        b'abcd++//'
        >>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
        b'abcd--__'
        >>> base64.urlsafe_b64decode('abcd--__')
        b'i\xb7\x1d\xfb\xef\xff'
     3. Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
        Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

> * struct

     1. struct
        可以将bytes和其他二进制数据类型的转换
     2. pack
        struct的pack函数把任意数据类型变成bytes：
        >>> import struct
        >>> struct.pack('>I', 10240099)
        b'\x00\x9c@c'

        pack的第一个参数是处理指令，'>I'的意思是：
        >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

        后面的参数个数要和处理指令一致。
        unpack把bytes变成相应的数据类型：
        >>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
        (4042322160, 32896)
        根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

> * hashlib

    1. MD5
        md5 = hashlib.md5()
        md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
        print(md5.hexdigest())
        d26a53750bc40b38b65a520292f69306
        MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
    2. SHA1
        sha1 = hashlib.sha1()
        sha1.update('how to use sha1 in '.encode('utf-8'))
        sha1.update('python hashlib?'.encode('utf-8'))
        print(sha1.hexdigest())
        SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

> * hmac

    1. md5(message + salt)
    2. hmac
        >>> message = b'Hello, world!'
        >>> key = b'secret'
        >>> h = hmac.new(key, message, digestmod='MD5')
        >>> # 如果消息很长，可以多次调用h.update(msg)
        >>> h.hexdigest()
        'fa4ee7d173f2d97ee79022d1a7355bcf'
        可见使用hmac和普通hash算法非常类似。
        hmac输出的长度和原始哈希算法的长度一致。
        需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

> * itertools

    1. count()
        natuals = itertools.count(1)
    2. cycle()
        cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    3. repeat()
         ns = itertools.repeat('A', 3)
    4. takewhile()
        根据条件判断来截取出一个有限的序列：
        >>> natuals = itertools.count(1)
        >>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
        >>> list(ns)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    5. chain()
        把一组迭代对象串联起来，形成一个更大的迭代器:
        >>> for c in itertools.chain('ABC', 'XYZ'):
        ...     print(c)
        # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
    6. groupby()
        把迭代器中相邻的重复元素挑出来放在一起：
        >>> for key, group in itertools.groupby('AAABBBCCAAA'):
        ...     print(key, list(group))
        ...
        A ['A', 'A', 'A']
        B ['B', 'B', 'B']
        C ['C', 'C']
        A ['A', 'A', 'A']
        挑选规则是通过函数完成的:
        >>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        ...     print(key, list(group))
        ...
        A ['A', 'a', 'a']
        B ['B', 'B', 'b']
        C ['c', 'C']
        A ['A', 'A', 'a']

> * contextlib

    1. 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
        实现上下文管理是通过__enter__和__exit__这两个方法实现的
        class Query(object):

            def __init__(self, name):
                self.name = name

            def __enter__(self):
                print('Begin')
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                if exc_type:
                    print('Error')
                else:
                    print('End')

            def query(self):
                print('Query info about %s...' % self.name)
        with Query('Bob') as q:
            q.query()
    2. @contextmanager
        class Query(object):
            def __init__(self, name):
                self.name = name
            def query(self):
                print('Query info about %s...' % self.name)

        @contextmanager
        def create_query(name):
            print('Begin')
            q = Query(name)
            yield q
            print('End')

        @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，
        然后，with语句就可以正常地工作了：
        with create_query('Bob') as q:
            q.query()
    3. 在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
        @contextmanager
        def tag(name):
            print("<%s>" % name)
            yield
            print("</%s>" % name)

        with tag("h1"):
            print("hello")
            print("world")

        上述代码执行结果为：
        <h1>
        hello
        world
        </h1>
    4. @closing
        urlopen()
        with closing(urlopen('https://www.python.org')) as page:
            for line in page:
                print(line)
    5. closing也是一个经过@contextmanager装饰的generator
        @contextmanager
           def closing(thing):
               try:
                   yield thing
               finally:
                   thing.close()

> * urllib

    1. request
        with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
            data = f.read()
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', data.decode('utf-8'))
    2. 往Request对象添加HTTP头
        req = request.Request('http://www.douban.com/')
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        with request.urlopen(req) as f:
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', f.read().decode('utf-8'))
    3. POST:把参数data以bytes形式传入
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
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

        with request.urlopen(req, data=login_data.encode('utf-8')) as f:
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', f.read().decode('utf-8'))
    4. Handler
        通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
        proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
        proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
        proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
        opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
        with opener.open('http://www.example.com/login.html') as f:
            pass

> * XML

    1. DOM vs SAX

> * HTMLParser

    1. HTMLParser
        利用HTMLParser，可以把网页中的文本、图像等解析出来。

