print('''---------------------使用@property---------------------
''')


# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):
    pass


s = Student()
s.score = 9999


# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于追求完美的Python程序员来说，这是必须要做到的！
#
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，
# 装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print("s.score = ", s.score)  # OK，实际转化为s.set_score(60)


# s.score = 9999 ********报错********


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
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


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
