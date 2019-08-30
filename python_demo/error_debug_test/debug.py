import logging

print('''---------------------调试---------------------
''')


# 需要一整套调试程序的手段来修复bug。

# 第一种 方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def main():
    foo('0')


# main()

# 第二种 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main1():
    foo1('0')


# main1()

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

# 第三种 logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
def foo2(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


def main2():
    foo2('0')


logging.basicConfig(level=logging.INFO)


# main2()

# 这就是logging的好处，它允许你指定记录信息的级别，
# 有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 第四种 pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# 执行方法：python -m pdb debug.py

# pdb.set_trace()

# **************小结**************
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
def test():
    print("使用方法一调试：", main())
    # print("使用方法二调试：", main1())
    # print("使用方法三调试：", main2())


test()
