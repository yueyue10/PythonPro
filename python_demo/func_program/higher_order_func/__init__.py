# 高阶函数
# 变量可以指向函数
print("abs(-10)=", abs(-10))
print("abs=", abs)
# 可见，abs(-10)是函数调用，而abs是函数本身。

f = abs
print("\nf(-10)=", f(-10))


# 传入函数
# 一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))
