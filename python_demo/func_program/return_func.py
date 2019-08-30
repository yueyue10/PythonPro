print('''---------------------返回函数---------------------
''')


# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
def lazy_sum(*args):
    def sumZ():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sumZ


f = lazy_sum(1, 3, 5, 7, 9)
print("f=", f)
print("f()=", f())


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
#
# 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print("\n")
print("f1()=", f1())
print("f2()=", f2())
print("f3()=", f3())


# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
#
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count1():
    def f1(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f1(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count1()
print("\n")
print("f1()=", f1())
print("f2()=", f2())
print("f3()=", f3())


def createCounter():
    li = [0]

    def counter():
        li.append(li[-1] + 1)
        return li[-1]

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
