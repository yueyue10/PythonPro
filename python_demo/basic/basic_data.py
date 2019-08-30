print('''---------------------数据类型和变量---------------------
''')

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，
# 所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看

print("转义字符串：I\'m \"OK\"!")
print('\\\t转义tab间隔\\')
# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试

print("\n", r'\\\t不进行转义\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：

print("\n", "使用\'\'\'进行包装表示多行内容", '''line1
... line2
... line3''')

# 布尔值
# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，
# 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
print("\n", "布尔值测试True：", True)
print("布尔值测试False：", False)
print("布尔值测试3 > 2：", 3 > 2)

# 布尔值可以用and、or和not运算。
# and运算是与运算，只有所有都为True，and运算结果才是True：
print("\n", "布尔值测试True and True：", True and True)
print("布尔值测试True and False：", True and False)
print("布尔值测试5 > 3 and 3 > 1：", 5 > 3 and 3 > 1)

# or运算是或运算，只要其中有一个为True，or运算结果就是True：
print("\n", "布尔值测试True or True：", True or True)
print("布尔值测试True or False：", True or False)
print("布尔值测试False or True：", False or True)

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print("\n", "布尔值测试not True：", not True)
print("布尔值测试not False：", not False)
print("布尔值测试not 1 > 2", not 1 > 2)

# 变量
# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：
a = 1
t_007 = 'T007'
Answer = True


# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
def test1():
    a = 123  # a是整数
    print("\na=", a)


def test2():
    a = 'ABC'
    b = a
    a = 'XYZ'
    print("\na=" + a)
    print("b=" + b)


test1()
test2()

# 常量
# 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
PI = 3.14159265359

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print("\n10 / 3=", 10 / 3)
print("9 / 3=", 9 / 3)
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print("\n10 // 3=", 10 // 3)
# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
print("\n10 % 3=", 10 % 3)
