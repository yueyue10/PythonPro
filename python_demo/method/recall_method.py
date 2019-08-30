print('''---------------------递归函数---------------------
''')


# 阶乘n! = 1 x 2 x 3 x ... x n
# fact(n)用递归的方式写出来就是:
def fact(n):
    if n == 1:
        return 1
    fn = n * fact(n - 1);
    print ("n=%s" % n, "fn=%s" % fn)
    return fn


fact(5)
print("\n")


# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# fact(1000) 报错：RecursionError: maximum recursion depth exceeded in comparison

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact_iter(num, product):
    if num == 1:
        return product
    fn = fact_iter(num - 1, num * product)
    print ("num=%s" % num, "fn=%s" % fn)
    return fn


fact_iter(5, 1)
print("\n")
fact_iter(100, 1)
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。