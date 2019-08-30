# 面向对象编程(Object Oriented Programming，简称OOP)
### 知识点总结

> * 类和实例

     1. 面向对象最重要的概念就是类（Class）和实例（Instance）
     2. __init__

> * 访问限制

     1. 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
     2. __xxx__ 是特殊变量

> * 继承和多态

     1. class Cat(Animal):
     2. “file-like object“就是一种鸭子类型

> * 获取对象信息

     1. type()
        type(123)
     2. type(123)==type(456)
     3. type(abs)==types.BuiltinFunctionType
     4. type(lambda x: x)==types.LambdaType
     5. isinstance()    class的继承关系
        isinstance(h, Animal)
     6. 判断一个变量是否list或者tuple：
        isinstance([1, 2, 3], (list, tuple))
     7. dir()
        获得一个对象的所有属性和方法，它返回一个包含字符串的list
     8. 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
        >>> hasattr(obj, 'x') # 有属性'x'吗？
        True
        >>> setattr(obj, 'y', 19) # 设置一个属性'y'
        >>> hasattr(obj, 'y') # 有属性'y'吗？
        True
        >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
        404

> * 实例属性和类属性

    1. 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
        class Student(object):
            def __init__(self, name):
                self.name = name

        s = Student('Bob')
        s.score = 90

