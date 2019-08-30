from contextlib import contextmanager, closing
from urllib.request import urlopen

print('''---------------------contextlib---------------------
''')
# Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
try:
    with open('/path/to/file', 'r') as f:
        f.read()
except Exception as e:
    print(e)


# *********** @contextmanager ***********
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：


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


# @contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
print("\ncontextmanager使用1：")
with create_query('Bob') as q:
    q.query()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


print("\ncontextmanager使用2：")
with tag("h1"):
    print("hello")
    print("world")

# *********** @closing ***********
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
print("\n@closing使用：")
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)
