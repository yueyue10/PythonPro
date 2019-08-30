# 函数式编程
### 知识点总结

> * 高阶函数

     1. map/reduce
     2. map()函数接收两个参数，一个是函数，一个是Iterable。map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
        def f(x):
        ...     return x * x
        r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        list(r)
     3. list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
     4. reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
        reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
     5. 把序列[1, 3, 5, 7, 9]变换成整数13579：
        def fn(x, y):
        ...     return x * 10 + y
        reduce(fn, [1, 3, 5, 7, 9])
     6. 把str转换为int的函数：
        def fn(x, y):
        ...     return x * 10 + y
        def char2num(s):
        ...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        ...     return digits[s]
        reduce(fn, map(char2num, '13579'))
     7. str2int函数：
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        def str2int(s):
            def fn(x, y):
                return x * 10 + y
            def char2num(s):
                return DIGITS[s]
            return reduce(fn, map(char2num, s))
        def str2int(s):
            def char2num(s):
                return DIGITS[s]
            return reduce(lambda x, y: x * 10 + y, map(char2num, s))

     1. filter()：用于过滤序列，返回一个Iterator
        def is_odd(n):
            return n % 2 == 1

        list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
     2. 把一个序列中的空字符串删掉：
        def not_empty(s):
            return s and s.strip()

        list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

     1. sorted()函数就可以对list进行排序
        >>> sorted([36, 5, -12, 9, -21])
        [-21, -12, 5, 9, 36]
     2. sorted()函数也是一个高阶函数
        >>> sorted([36, 5, -12, 9, -21], key=abs)
        [5, 9, -12, -21, 36]
     3. 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
        >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
        ['Zoo', 'Credit', 'bob', 'about']

> * 返回函数

     1. 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
        def lazy_sum(*args):
            def sum():
                ax = 0
                for n in args:
                    ax = ax + n
                return ax
            return sum
        f = lazy_sum(1, 3, 5, 7, 9)
        >>> f()
        25
     2. 闭包
         返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
         def count():
             def f(j):
                 def g():
                     return j*j
                 return g
             fs = []
             for i in range(1, 4):
                 fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
             return fs

         >>> f1, f2, f3 = count()
         >>> f1()
         1
         >>> f2()
         4
         >>> f3()
         9

> * 匿名函数

     1. 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
        匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
     2. 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
        f = lambda x: x * x
        >>> f(5)
        25

> * 装饰器

     1. 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
        >>> def now():
        ...     print('2015-3-25')
        ...
        >>> f = now
     2. 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
     3. decorator就是一个返回函数的高阶函数
        def log(func):
            def wrapper(*args, **kw):
                print('call %s():' % func.__name__)
                return func(*args, **kw)
            return wrapper
        @log
        def now():
            print('2015-3-25')
        >>> now()
        call now():
        2015-3-25

        把@log放到now()函数的定义处，相当于执行了语句：
        now = log(now)

> * 偏函数(Partial function)

    1. functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
    2. int2 = functools.partial(int, base=2)
       int2('10010')
       相当于：
       kw = { 'base': 2 }
       int('10010', **kw)
    3. max2 = functools.partial(max, 10)
       max2(5, 6, 7)=10
       args = (10, 5, 6, 7)
       max(*args)

