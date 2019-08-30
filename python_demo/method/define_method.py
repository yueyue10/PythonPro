print('''---------------------定义函数---------------------
''')


def my_abs(x):
    print("\n---------------------define_method定义函数---------------------")
    if x >= 0:
        return x
    else:
        return -x
    print(my_abs(-99))


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass


age = 100
if age >= 18:
    pass


# 参数检查
# my_abs("A")  #报错不明显
# 修改后的函数
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 导入math包，并允许后续代码引用math包里的sin、cos等函数。
import math


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print("x, y=", x, y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print("r=", r)


# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


print("\nquadratic函数测试：")
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
