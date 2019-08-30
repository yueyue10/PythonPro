import functools

print('''---------------------偏函数---------------------
''')

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print("int('12345')=", int('12345'))
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print("int('12345', base=8)=", int('12345', base=8))


# 定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)


print("int2('1000000')=", int2('1000000'))
print("int2('1010101')=", int2('1010101'))

# functools.partial就是帮助我们创建一个偏函数的，
#
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
int22 = functools.partial(int, base=2)
print("\n")
print("int22('1000000')=", int22('1000000'))

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
max10 = functools.partial(max, 10)
print("max10(5, 6, 7)=", max10(5, 6, 7))
