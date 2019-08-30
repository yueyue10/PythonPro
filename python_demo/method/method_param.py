print('''---------------------函数的参数---------------------
''')


# 位置参数
# 计算x2的函数：
def power(x):
    return x * x


print ("power(5)=", power(5))
print ("power(15)=", power(15))


# 用来计算x的n次方
# power(x, n)函数有两个参数：x和n，这两个参数都是位置参数
def powern(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print ("\npower(5, 2)=", powern(5, 2))
print ("power(5, 3)=", powern(5, 3))


# 默认参数
def powern1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


str = "powern1(5,2)= %s powern1(5)=%s"
p5 = powern1(5)
p52 = powern1(5, 2)
print ("\npowern1(x, n=2)函数测试：", str % (p5, p52))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:%s gender:%s age:%s city:%s' % (name, gender, age, city))


print ("\nenroll函数测试：")
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L


print ("add_end函数测试：", add_end([1, 2, 3]))
print (add_end(['x', 'y', 'z']))
print (add_end())
print (add_end())


# 修改上面的例子，我们可以用None这个不变对象来实现：
def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print ("add_end1函数测试：", add_end1())
print (add_end1())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print ("\ncalc(1, 3, 5, 7)=", calc(1, 3, 5, 7))
nums = [1, 2, 3]
print ("calc(*nums)=", calc(*nums))


# 关键字参数(传入key-value类参数)
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 关键字参数可以作为可选项参数使用
print ("\nperson关键字参数测试：")
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
# 作用：检查是关键字参数是否含有特定参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)