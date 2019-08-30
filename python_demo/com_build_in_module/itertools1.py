import itertools

print('''---------------------itertools---------------------
''')
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#     1
#     2
#     3
#     ...
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)
#     'A'
#     'B'
#     'C'
#     'A'
#     'B'
#     'C'
#     ...
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# itertools提供的几个迭代器操作函数更加有用：

# *********** chain() ***********
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
print("\nchain使用：")
for c in itertools.chain('AB', 'XY'):
    print(c)

# *********** groupby() ***********
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
print("\ngroupby使用：")
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
print("\ngroupby自定义使用：")
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# 练习
# 计算圆周率可以根据公式：
#
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
print("\n")


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    na = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    nss = itertools.takewhile(lambda x: x <= 2 * N - 1, na)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    pm = list(nss)
    result = list(map(lambda x: float(4 / x * 1 if pm.index(x) % 2 == 0 else 4 / x * -1), pm))
    return sum(result)
    # ' 计算pi的值 '
    # # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # odds = itertools.count(1,2)
    # # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # ns = itertools.takewhile(lambda x: x <= (2 * N -1), odds)
    # # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # pm =list(ns)
    # result = list(map(lambda x: float(4 / x * 1 if pm.index(x) % 2 == 0 else 4 / x * -1), pm))
    # # step 4: 求和:
    # return sum(result)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
