from collections import Iterable

print('''---------------------迭代---------------------
''')

# 在Python中，迭代是通过for ... in来完成的，
d = {'a': 1, 'b': 2, 'c': 3}  # key-value键值对
for key in d:
    print("key=", key)

for value in d.values():
    print("value=", value)

for k, v in d.items():
    print("key=%s,value=%s" % (k, v))

for ch in 'ABC':
    print(ch)

# 通过collections模块的Iterable类型判断一个对象是可迭代对象
print ("\n", isinstance('abc', Iterable))  # str是否可迭代
print (isinstance([1, 2, 3], Iterable))  # list是否可迭代
print (isinstance(123, Iterable))  # 整数是否可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
print("\n")
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for循环里，同时引用了两个变量
print("\n")
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    if len(L)==0:
        return None, None
    else:
        max = L[0]
        min = L[0]
        print ("max=", max)
        for l in L:
            if l>max:
                max=l
            if l<min:
                min=l
        return max,min

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')