import os

print('''---------------------列表生成式---------------------
''')

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))

# 要生成[1x1, 2x2, 3x3, ..., 10x10]
#
# 方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print("\nL=", L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用
L1 = [x * x for x in range(1, 11)]
print("\nL1=", L1)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print("\nL2=", L2)

# 还可以使用两层循环，可以生成全排列：
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print("\nL3=", L3)

# 运用列表生成式，可以写出非常简洁的代码。
L4 = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print("\nL4=", L4)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 列表生成式也可以使用两个变量来生成list：
L5 = [k + '=' + v for k, v in d.items()]
print("\nL5=", L5)

# 最后把一个list中所有的字符串变成小写：
L6 = ['Hello', 'World', 18, 'IBM', 'Apple']
L6 = [s.lower() for s in L6 if isinstance(s, str)]
print("\nL6=", L6)
