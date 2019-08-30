print('''---------------------使用dict和set---------------------
''')
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print ("d['Michael']:", d['Michael'])

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print ("d['Adam']:", d['Adam'])

# 如果key不存在，dict就会报错：
# d['Thomas'] KeyError: 'Thomas'

# 判断key不存在的 一是通过in判断key是否存在：
print ("\n使用in判断key是否存在", 'Thomas' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print ("\n使用get获取value", d.get('Thomas', -1))

# dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

