print('''---------------------生成器---------------------
''')
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print("\nL=", L)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x * x for x in range(10))
print("\ng=", g)
print("\nnext(g)=", next(g))
print("\nnext(g)=", next(g))
# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
for n in g:
    print(n)


# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print("\nfib1=")
for n in fib1(6):
    print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
print("\n")
g1 = fib1(6)
while True:
    try:
        x = next(g1)
        print('g1:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


print("\n")
o = odd()
next(o)
next(o)
next(o)

# 生成杨辉三角
def triangles(line):
    n, i = 0, 1
    ll = [1]
    while n < line:
        print(ll)
        ll.append(1)
        for i, l in enumerate(ll):
            if i - 1 >= 0 & i < len(ll):
                ll[i] = ll[i - 1] + ll[i]
        n = n + 1
    return "done"


triangles(3)


def triangles():
    ll = [1]
    for i, l in enumerate(ll):
        yield ll
        ll.append(1)
        if i - 1 >= 0 & i < len(ll):
            ll[i] = ll[i - 1] + ll[i]


t = triangles()
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
