# 面向对象高级编程
### 知识点总结

> * 使用__slots__

     1. MethodType
        >>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
        >>> Student.set_score = set_score   为了给所有实例都绑定方法，可以给class绑定方法：
     2. __slots__   限制实例的属性
        class Student(object):
            __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

> * 使用@property

     1. raise
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
     2. @property装饰器
        负责把一个方法变成属性调用的：
        class Student(object):
            @property
            def score(self):
                return self._score
     3. 可读写属性   只读属性
        class Student(object):

            @property
            def birth(self):
                return self._birth

            @birth.setter
            def birth(self, value):
                self._birth = value

            @property
            def age(self):
                return 2015 - self._birth
        上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

> * 多重继承

     1. 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
        class Dog(Mammal, Runnable):
            pass
     2. MixIn

> * 定制类

     1. __xxx__
     2. __str__
        __str__()   打印的时候会调用
     3. __repr__()
     4. __iter__
        一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
     5. __getitem__
        当成list来使用其按照下标取出元素的方法，需要实现__getitem__()方法：
     6. __getattr__
        当我们调用类的方法或属性时，如果不存在，就会报错。
        Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
     7. __call__
        一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
        任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
        class Student(object):
            def __init__(self, name):
                self.name = name

            def __call__(self):
                print('My name is %s.' % self.name)
        调用方式如下：

        >>> s = Student('Michael')
        >>> s() # self参数不要传入
        My name is Michael.
     8. callable()
        判断一个变量是对象还是函数.通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

> * 使用枚举类

    1. 当我们需要定义多个常量时,Python提供了Enum类来实现这个功能:
       Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
       for name, member in Month.__members__.items():
           print(name, '=>', member, ',', member.value)
       value属性则是自动赋给成员的int常量，默认从1开始计数。
       >>> day1 = Weekday.Mon
       >>> print(day1)
       Weekday.Mon
       >>> print(Weekday.Tue)
       Weekday.Tue
       >>> print(Weekday['Tue'])
       Weekday.Tue
       >>> print(Weekday.Tue.value)
       2
       >>> print(day1 == Weekday.Mon)
       True

> * 使用元类

    1. type()
       type()函数既可以返回一个对象的类型，又可以创建出新的类型
       >>> def fn(self, name='world'): # 先定义函数
       ...     print('Hello, %s.' % name)
       ...
       >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
    2. 动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同
    3. metaclass
    4. d['Michael'] = 35
    5. 'Michael' in d
    6. d.get('Thomas', -1)
    7. d.pop('Bob')
    8. set1 = set([1, 2, 3])
    9. set1.add(4)
    10. set1.remove(4)
    11. set1 & set2
    12. set1 | set2
    13. ['c', 'b', 'a'].sort()
