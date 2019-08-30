#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'zhaoyj'
print('''---------------------类和实例---------------------
''')


# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
#
# 第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

# 仍以Student类为例，在Python中，定义类是通过class关键字：
#
class Student(object):
    pass


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
bart = Student()
print("bart=", bart)
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = 'Bart Simpson'
print("bart.name=", bart.name)


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，
#
# 把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，
#
# 在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
# 必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
bart = Student('Bart Simpson', 59)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print("\n")
print_score(bart)


# 数据封装
# 既然Student实例本身就拥有这些数据，要访问这些数据，
# 就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
# 这样，就把“数据”给封装起来了。
class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'grade A'
        elif self.score >= 60:
            return 'grade B'
        else:
            return 'grade C'


bart1 = Student1('Bart Simpson1', 591)
bart1.print_score()
# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
lisa = Student1('Lisa', 99)
bart = Student1('Bart', 59)
print("\n", lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
