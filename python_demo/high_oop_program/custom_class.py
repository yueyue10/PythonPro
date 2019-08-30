print('''---------------------定制类--------------------
''')


# __str__
class Student(object):
    def __init__(self, name):
        self.name = name


def __str__(self):
    return 'Student object (name: %s)' % self.name


print(Student('Michael'))
Student.__str__ = __str__  #
print(Student('Michael'))

s = Student('Michael')
print("s=", s)


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


print("\n__iter__使用：")
for n in Fib():
    print(n)


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# Fib()[5] ***报错：TypeError: 'Fib' object is not subscriptable
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


print("\n__getitem__使用：")
print("Fib()[0]=", Fib()[0])
print("Fib()[1]=", Fib()[1])


# Fib()[0, 5]
# 报错：TypeError: 'tuple' object cannot be interpreted as an integer

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print("\n__getitem__处理切片使用：")
print("Fib()[0:5]=", Fib()[0:5])


# __getattr__

# 当我们调用类的方法或属性时，如果不存在，就会报错
# 错误信息很清楚地告诉我们，没有找到score这个attribute。
#
# 要避免这个错误，除了可以加上一个score属性外，
# Python还有另一个机制，
# 那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25  # 返回函数也是完全可以的：


# 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
s = Student()
print("\n__getattr__使用：")
print("s.name=%s,s.score=%s" % (s.name, s.score))
print("s.age()=", s.age())


# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print("__getattr__结合Chain()使用：", Chain().status.user.timeline.list)


# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('\n调用类的实例：My name is %s.' % self.name)


s = Student('Michael')
s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
#
# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print("\n判断一个对象是否是“可调用”对象:")
print(callable(Student('Michael')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
