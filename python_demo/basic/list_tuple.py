print('''---------------------使用list和tuple---------------------
''')

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print("classmates:", classmates)
# 变量classmates就是一个list。用len()函数可以获得list元素的个数：

print("classmates长度：", len(classmates))
print("classmates[0]:", classmates[0])
# print ("classmates[3]:", classmates[3])  报错IndexError: list index out of range

# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print("classmates最后一位:", classmates[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
print("\nclassmates插入:", classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print("classmates:", classmates)

# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print("\nclassmates移除:", classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print("classmates:", classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print("\nclassmates替换:", classmates)

# list里面的元素的数据类型也可以不同，比如：
list = ['Apple', 123, True]
print("\nlist里面的元素的数据类型也可以不同:", list)

# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print("\nlist元素也可以是另一个list:", s)

print("\n", '''---------------------另一种有序列表叫元组：tuple.tuple一旦初始化就不能修改---------------------
''')
classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
