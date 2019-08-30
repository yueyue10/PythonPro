import types

print('''---------------------获取对象信息---------------------
''')
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

# 一、使用type()
# 首先，我们来判断对象类型，使用type()函数：
#
# 基本类型都可以用type()判断：
print("type(123)=", type(123))
print("type(abs)=", type(abs))
# type()函数返回的是对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print("\n")
print("type(123)==type(456)", type(123) == type(456))
print("type('abc')==str", type('abc') == str)


def fn():
    pass


print("\n")
print("type(fn)==types.FunctionType", type(fn) == types.FunctionType)
print("type(lambda x: x)==types.LambdaType", type(lambda x: x) == types.LambdaType)
print("type((x for x in range(10)))==types.GeneratorType", type((x for x in range(10))) == types.GeneratorType)

# 二、使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。
#
# 我们要判断class的类型，可以使用isinstance()函数。
# object -> Animal -> Dog -> Husky
# a = Animal()
# d = Dog()
# h = Husky()
# >>> isinstance(h, Husky)
# True
print("\n")
print("isinstance('a', str)", isinstance('a', str))
print("isinstance(b'a', bytes)", isinstance(b'a', bytes))

# 并且还可以判断一个变量是否是某些类型中的一种，
#
# 比如下面的代码就可以判断是否是list或者tuple：
print("\n")
print("isinstance([1, 2, 3], (list, tuple))", isinstance([1, 2, 3], (list, tuple)))
print("isinstance((1, 2, 3), (list, tuple))", isinstance((1, 2, 3), (list, tuple)))
# ******总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 三、使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print("\n")
print("dir('ABC')", dir('ABC'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print("len('ABC')=", len('ABC'))
print("'ABC'.__len__()=", 'ABC'.__len__())


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 紧接着，可以测试该对象的属性：
print("\n")
print("obj有属性'x'吗？", hasattr(obj, 'x'))
print("obj有属性'y'吗？", hasattr(obj, 'y'))
print("\n设置一个属性'y'", setattr(obj, 'y', 19))
print("obj有属性'y'吗？", hasattr(obj, 'y'), "获取属性'y'", obj.y)

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z')  # 获取属性'z'
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print("\n获取属性'z'，如果不存在，返回默认值404-->", getattr(obj, 'z', 404))

# 也可以获得对象的方法：
print("\n有属性'power'吗？", hasattr(obj, 'power'))
print("获取属性'power'-->", getattr(obj, 'power'))
# 返回bound method MyObject.power of证明是一个方法
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print("fn()=", fn())
