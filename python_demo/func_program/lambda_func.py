print('''---------------------匿名函数---------------------
''')
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("L=", L)


# 通过对比可以看出，匿名函数lambda x: x * x实际上就是：
#
def fun(x):
    return x * x


# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print("\nf=", f)
print("f(5)=", f(5))


# 同样，也可以把匿名函数作为返回值返回，比如：
#
def build(x, y):
    return lambda: x * x + y * y


# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1


LL = list(filter(is_odd, range(1, 20)))
LL1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(LL)
print(LL1)
