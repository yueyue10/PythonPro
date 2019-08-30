print('''---------------------继承和多态---------------------
''')


# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()
# 要理解什么是多态，我们首先要对数据类型再作一点说明。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
# 判断一个变量是否是某个类型可以用isinstance()判断：
print("\n")
print("isinstance(a, list)=", isinstance(a, list))
print("isinstance(b, Animal)=", isinstance(b, Animal))
print("isinstance(c, Dog)=", isinstance(c, Dog))
print("isinstance(c, Animal)=", isinstance(c, Animal))
# 看来c不仅仅是Dog，c还是Animal！
