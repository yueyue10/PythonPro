import logging

print('''---------------------错误处理---------------------
''')
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。
# 比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

# try
try:
    print('try...')
    r = 10 / 0  # 0可以改为2试一下
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


# 调用栈
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


# main()
# ******报错******：
# line 25, in foo
# return 10 / int(s)
# ZeroDivisionError: division by zero

# 记录错误
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# main()
print('main END')


# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

# 抛出错误
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
