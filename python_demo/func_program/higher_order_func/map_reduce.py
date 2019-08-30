from functools import reduce

print('''---------------------map/reduce---------------------
''')


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#                            f(x) = x * x
#                                 │
#                                 │
# ┌───┬───┬───┬───┼───┬───┬───┬───┐
# │      │      │      │      │      │      │      │      │
# ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
# [1      2        3      4        5       6       7      8       9 ]
# │      │      │      │      │      │      │      │      │
# │      │      │      │      │      │      │      │      │
# ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
# [1      4        9      16      25      36      49      64      81 ]

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list(r)=", list(r))
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。

# map()作为高阶函数，事实上它把运算规则抽象了，
#
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print("list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))=", list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：
def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print("\nreduce(add, [1, 3, 5, 7, 9])=", reduce(add, [1, 3, 5, 7, 9]))
print("reduce(fn, [1, 3, 5, 7, 9])=", reduce(fn, [1, 3, 5, 7, 9]))
print("reduce(fn, map(char2num, '13579'))=", reduce(fn, map(char2num, '13579')))  # 把str转换为int的函数

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn1(x, y):
        return x * 10 + y

    def char2num1(s):
        return DIGITS[s]

    return reduce(fn1, map(char2num1, s))


# 还可以用lambda函数进一步简化成：
def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2float(s):
    return reduce(lambda x, y: x * 0.1 + y, map(char2num, s))


print("\nstr2int1('2345324')=", str2int1("2345324"))  # 把str转换为int的函数


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    name = name.lower()
    f = name[:1].upper()
    n = name[1:]
    return f + n


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print("\nL2=", L2)


# 编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('\n3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    s1, s2 = s.split('.')

    return reduce(lambda x, y: x * 10 + y, map(char2num, s1)) + reduce(lambda x, y: x * 10 + y, map(char2num, s2)) / (
            10 ** len(s2))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
