# 条件判断
# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
print('''---------------------条件判断---------------------
''')
age = 20
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
print ("if语句")
if age >= 18:
    print('your age is', age)
    print('adult')

print ("\nif-else语句")
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# 再议 input
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
s = input('\n请输入birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
