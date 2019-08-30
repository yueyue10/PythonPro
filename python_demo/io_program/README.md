# IO编程
### 知识点总结

> * 文件读写

     1. open()
        >>> f = open('/Users/michael/test.txt', 'r')
     2. read()
        Python把内容读到内存，用一个str对象表示：
        >>> f.read()
        'Hello, world!'
     3. close()
        >>> f.close()
     4. with
        with open('/path/to/file', 'r') as f:
            print(f.read())
     5. 如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
        for line in f.readlines():
            print(line.strip()) # 把末尾的'\n'删掉
     6. file-like Object
     7. 二进制文件
        要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
        >>> f = open('/Users/michael/test.jpg', 'rb')
        >>> f.read()
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
     8. 字符编码
        要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
        >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
        >>> f.read()
        '测试'
     9. 写文件
        写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
        >>> f = open('/Users/michael/test.txt', 'w')
        >>> f.write('Hello, world!')
        >>> f.close()
     10.    append

> * StringIO和BytesIO

     1. StringIO顾名思义就是在内存中读写str。
        >>> f = StringIO()
        >>> f.write('hello')
        5
        >>> f.write(' ')
        1
        >>> f.write('world!')
        6
        >>> print(f.getvalue())
        hello world!
     2. write()
     3. getvalue()
        >>> from io import StringIO
        >>> f = StringIO('Hello!\nHi!\nGoodbye!')
        >>> while True:
        ...     s = f.readline()
        ...     if s == '':
        ...         break
        ...     print(s.strip())
        ...
        Hello!
        Hi!
        Goodbye!
     4. BytesIO
        操作二进制数据,BytesIO实现了在内存中读写bytes
        >>> f = BytesIO()
        >>> f.write('中文'.encode('utf-8'))
        6
        >>> print(f.getvalue())
        b'\xe4\xb8\xad\xe6\x96\x87'
     5.和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
       >>> from io import BytesIO
       >>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
       >>> f.read()
       b'\xe4\xb8\xad\xe6\x96\x87'

> * 操作文件和目录

     1. Python内置的os模块也可以直接调用操作系统提供的接口函数。
        >>> os.name # 操作系统类型
        'posix'
        如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
     2. os.environ
        环境变量
     3. 操作文件和目录
        把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
     4. os.path.split()
     5. os.path.splitext()
        可以直接让你得到文件扩展名
     6. shutil  copyfile()
     7. 列出当前目录下的所有目录
        >>> [x for x in os.listdir('.') if os.path.isdir(x)]
        ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
     8. 要列出所有的.py文件，也只需一行代码：
        >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
        ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

> * 序列化

     1. pickling
     2. pickle.dumps()
        把任意对象序列化成一个bytes
        >>> d = dict(name='Bob', age=20, score=88)
        >>> pickle.dumps(d)
        b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
     3. pickle.dump()
        直接把对象序列化后写入一个file-like Object：
        >>> f = open('dump.txt', 'wb')
        >>> pickle.dump(d, f)
        >>> f.close()
     4. pickle.loads()
        将bytes反序列化出对象
     5. pickle.load()
        从一个file-like Object中直接反序列化出对象。
        >>> f = open('dump.txt', 'rb')
        >>> d = pickle.load(f)
        >>> f.close()
        >>> d
        {'age': 20, 'score': 88, 'name': 'Bob'}
     6. json.dumps(d)
        把Python对象变成一个JSON，dumps()方法返回一个str，内容就是标准的JSON。
        >>> d = dict(name='Bob', age=20, score=88)
        >>> json.dumps(d)
        '{"age": 20, "score": 88, "name": "Bob"}'
     7. dump()方法可以直接把JSON写入一个file-like Object。
     8. 要把JSON反序列化为Python对象，
        用loads()或者对应的load()方法，
        >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        >>> json.loads(json_str)
        {'age': 20, 'score': 88, 'name': 'Bob'}
     9. 上面的dict对象可以直接序列化为JSON的{}，
        下面将class对象序列化
        class Student(object):
            def __init__(self, name, age, score):
                self.name = name
                self.age = age
                self.score = score

        def student2dict(std):
            return {
                'name': std.name,
                'age': std.age,
                'score': std.score
            }
        s = Student('Bob', 20, 88)
        >>> print(json.dumps(s, default=student2dict))
        {"age": 20, "name": "Bob", "score": 88}
        可简写为(把任意class的实例变为dict)：
        print(json.dumps(s, default=lambda obj: obj.__dict__))
     10. 把JSON反序列化为一个Student对象实例
          def dict2student(d):
              return Student(d['name'], d['age'], d['score'])
          >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
          >>> print(json.loads(json_str, object_hook=dict2student))
          <__main__.Student object at 0x10cd3c190>

