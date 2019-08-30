# 常用第三方模块
### 知识点总结

> * Pillow

     1. 操作图像
        # 打开一个jpg图像文件，注意是当前路径:
        im = Image.open('test.jpg')
        # 获得图像尺寸:
        w, h = im.size
        print('Original image size: %sx%s' % (w, h))
        # 缩放到50%:
        im.thumbnail((w//2, h//2))
        print('Resize image to: %sx%s' % (w//2, h//2))
        # 把缩放后的图像用jpeg格式保存:
        im.save('thumbnail.jpg', 'jpeg')
     2. 模糊效果
        # 打开一个jpg图像文件，注意是当前路径:
        im = Image.open('test.jpg')
        # 应用模糊滤镜:
        im2 = im.filter(ImageFilter.BLUR)
        im2.save('blur.jpg', 'jpeg')
     3. ImageDraw
        PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

> * requests

     1. GET
        >>> r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
        >>> r.url # 实际请求的URL
        'https://www.douban.com/search?q=python&cat=1001'
        >>> r.encoding
        'utf-8'
        >>> r.content
        b'<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n...'
     2. requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
        >>> r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
        >>> r.json()
        {'query': {'count': 1, 'created': '2017-11-17T07:14:12Z', ...
     3. 需要传入HTTP Header时
        我们传入一个dict作为headers参数：
        >>> r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
        >>> r.text
        '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n <title>豆瓣(手机版)</title>...'
     4. POST
        >>> r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
     5. 传递JSON数据
        requests默认使用application/x-www-form-urlencoded对POST数据编码.
        要传递JSON数据，可以直接传入json参数：
        params = {'key': 'value'}
        r = requests.post(url, json=params) # 内部自动序列化为JSON
     6. 上传文件，requests把它简化成files参数：
        >>> upload_files = {'file': open('report.xls', 'rb')}
        >>> r = requests.post(url, files=upload_files)
     7. 获取HTTP响应的其他信息也非常简单
        >>> r.headers
        {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
        >>> r.headers['Content-Type']
        'text/html; charset=utf-8'
        >>> r.cookies['ts']
        'example_cookie_12345'
     8. 传入Cookie
        >>> cs = {'token': '12345', 'status': 'working'}
        >>> r = requests.get(url, cookies=cs)
     9. 指定超时
        >>> r = requests.get(url, timeout=2.5) # 2.5秒后超时

> * chardet

     1. chardet
        检测编码
        >>> chardet.detect(b'Hello, world!')
        {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
     2. 检测GBK编码的中文：
        >>> data = '离离原上草，一岁一枯荣'.encode('gbk')
        >>> chardet.detect(data)
        {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
     3. 对UTF-8编码进行检测：
        >>> data = '离离原上草，一岁一枯荣'.encode('utf-8')
        >>> chardet.detect(data)
        {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

> * psutil

    1. 获取CPU信息
        >>> psutil.cpu_count() # CPU逻辑数量
        4
        >>> psutil.cpu_count(logical=False) # CPU物理核心
        2
        # 2说明是双核超线程, 4则是4核非超线程
        >>> psutil.cpu_times() # 统计CPU的用户／系统／空闲时间：
        scputimes(user=10963.31, nice=0.0, system=5138.67, idle=356102.45)
    2. 获取内存信息
        使用psutil获取物理内存和交换内存信息，分别使用：
        >>> psutil.virtual_memory()
        svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
        >>> psutil.swap_memory()
        sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)
    3. 获取磁盘信息
        >>> psutil.disk_partitions() # 磁盘分区信息
        [sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
        >>> psutil.disk_usage('/') # 磁盘使用情况
        sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
        >>> psutil.disk_io_counters() # 磁盘IO
        sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)
    4. 获取网络信息
        >>> psutil.net_io_counters() # 获取网络读写字节／包的个数
        snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)
        >>> psutil.net_if_addrs() # 获取网络接口信息
        >>> psutil.net_if_stats() # 获取网络接口状态
    5. 获取进程信息
        >>> psutil.pids() # 所有进程ID
        [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
        >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
        >>> p.name() # 进程名称
        'python3.6'
        >>> p.exe() # 进程exe路径
        '/Users/michael/anaconda3/bin/python3.6'
        >>> p.cwd() # 进程工作目录
        '/Users/michael'
        >>> p.cmdline() # 进程启动的命令行
        ['python3']
        >>> p.ppid() # 父进程ID
        3765
        >>> p.parent() # 父进程
        <psutil.Process(pid=3765, name='bash') at 4503144040>
        >>> p.children() # 子进程列表
        []
        >>> p.status() # 进程状态
        'running'
        >>> p.username() # 进程用户名
        'michael'
        >>> p.create_time() # 进程创建时间
        1511052731.120333
        >>> p.terminal() # 进程终端
        '/dev/ttys002'
        >>> p.cpu_times() # 进程使用的CPU时间
        pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
        >>> p.memory_info() # 进程使用的内存
        pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)

