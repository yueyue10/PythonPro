print('''---------------------使用元类---------------------
''')
# type()
# 1.type()函数可以查看一个类型或变量的类型

# 2.要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。