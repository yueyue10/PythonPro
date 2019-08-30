import functools

print('''---------------------装饰器---------------------
''')


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now(): print('2015-3-25')


f = now
f()
print("now.__name__", now.__name__)
print("f.__name__", f.__name__)


# 现在，假设我们要增强now()函数的功能，
#
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#
# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，
#
# 并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def nowTime():
    print('2015-3-25')


print("\n")
nowTime()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def nowT():
    print('2015-3-25')


print("\n")
nowT()


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
# 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
#
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
