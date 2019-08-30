# 函数
### 知识点总结

> * 调用函数

     1. abs()
     2. max()
     3. int('123')
     4. str(100)
     5. bool(1)

> * 定义函数

     1. def
     2. pass
     3. return nx, ny
        -tuple

> * 函数的参数

     1. 位置参数
        def power(x):
     2. 默认参数
        def power(x, n):
     3. def add_end(L=[]):
        定义默认参数要牢记一点：默认参数必须指向不变对象！
        def add_end(L=None):
     4. 可变参数
        def calc(*numbers):
        nums = [1, 2, 3]
        calc(*nums)
     5. 关键字参数
        def person(name, age, **kw):
        person('Michael', 30)
        person('Bob', 35, city='Beijing')
        多个关键字参数1：person('Adam', 45, gender='M', job='Engineer')
        extra = {'city': 'Beijing', 'job': 'Engineer'}
        多个关键字参数2：person('Jack', 24, **extra)
     6. 命名关键字参数
        def person(name, age, **kw):
            if 'city' in kw:
                # 有city参数
                pass
     7. 参数组合
        参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
        def f1(a, b, c=0, *args, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
        args = (1, 2, 3, 4)
        kw = {'d': 99, 'x': '#'}
        f1(*args, **kw)
        >>> a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

> * 递归函数

     1. 递归函数
        def fact(n):
            if n==1:
                return 1
            return n * fact(n - 1)
     2. 尾递归
        def fact(n):
            return fact_iter(n, 1)

        def fact_iter(num, product):
            if num == 1:
                return product
            return fact_iter(num - 1, num * product)

