#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'zhaoyj'
print('''---------------------类和实例---------------------
''')


# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
#
# 只有内部可以访问，外部不能访问，所以，我们把Student类改一改
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：
bart = Student('Bart Simpson', 59)


# bart.__name 访问不到了
# 你也许会问，原先那种直接通过bart.score = 99也可以修改啊，
# 为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
# class Student(object):
#     ...
def set_score(self, score):
    if 0 <= score <= 100:
        self.__score = score
    else:
        raise ValueError('bad score')
# 在Python中，变量名类似__xxx__的，是特殊变量，特殊变量是可以直接访问的，不是private变量
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
