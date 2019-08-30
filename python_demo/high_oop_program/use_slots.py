from types import MethodType

print('''---------------------使用__slots__---------------------
''')


# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print("s.name=", s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# 尝试给实例绑定一个方法：
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print("# 测试结果:s.age=", s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例


# s2.set_age(25)  # 尝试调用方法
#
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print("\n")
print("s.score=", s.score)
s2.set_score(99)
print("s2.score=", s2.score)


# *******使用__slots__*******
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性

# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'


# s.score = 99 # 绑定属性'score'
# !!!报错 AttributeError: 'Student' object has no attribute 'score'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
