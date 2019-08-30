from socketserver import TCPServer, ForkingMixIn

print('''---------------------多重继承---------------------
''')


# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Parrot(Bird):
    pass


# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass


# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：

class Bat(Mammal, Flyable):
    pass


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn 混合继承
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
