# 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
from define_method import my_abs

print('''---------------------调用函数---------------------
''', "http://docs.python.org/3/library/functions.html#abs")

# abs max
print ("\nint('123')=", int('123'))
print ("float('12.34')=", float('12.34'))
print ("str(1.23)=", str(1.23))
print ("bool(1)=", bool(1))
print ("bool('')=", bool(''))

print ("\nhex" + hex(255))
print("使用define_method中的函数", my_abs(-99))
