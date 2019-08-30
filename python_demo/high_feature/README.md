# 高级特性
### 知识点总结

> * 切片

        L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
     1. L[0:3] 或 L[:3]
        前3个元素
     2. L[1:3]
     3. L[-1]
     4. L[-10:]
        后10个数：
     5. L[:10:2]
        前10个数，每两个取一个
     6. L[::5]
        所有数，每5个取一个：
     7. [:]
        原样复制一个list

> * 迭代

     1. 在Python中，迭代是通过for ... in
     2. 默认情况下，dict迭代的是key
        d = {'a': 1, 'b': 2, 'c': 3}
        如果要迭代value，可以用for value in d.values()
        如果要同时迭代key和value，可以用for k, v in d.items()
     3. for ch in 'ABC':
     4. Iterable
        可迭代对象
     5. isinstance('abc', Iterable) # str是否可迭代
     6. enumerate
        把一个list变成索引-元素对
     7. for i, value in enumerate(['A', 'B', 'C']):
     8. for循环里，同时引用了两个变量
        for x, y in [(1, 1), (2, 4), (3, 9)]:

> * 列表生成式

     1. list(range(1, 11)) 或者 [d for d in range(1, 11)]
        =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     2. [x * x for x in range(1, 11)]
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
     3. [x * x for x in range(1, 11) if x % 2 == 0]
        [4, 16, 36, 64, 100]
     4. [m + n for m in 'ABC' for n in 'XYZ']
        ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
     5. [d for d in os.listdir('.')]
     6. d = {'x': 'A', 'y': 'B', 'z': 'C' } [k + '=' + v for k, v in d.items()]
        =['y=B', 'x=A', 'z=C']
     7. L = ['Hello', 'World', 'IBM', 'Apple'] [s.lower() for s in L]
        =['hello', 'world', 'ibm', 'apple']

> * 条件判断

     1. elif是else if的缩写
     2. str=input()

> * 生成器

    1. 在Python中，这种一边循环一边计算的机制，称为生成器：generator
        g = (x * x for x in range(10))
    2. next(g)
    3. for n in g:
    4. yield

> * 迭代器

    1. 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    2. isinstance([], Iterator)
    3. 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
        把list、dict、str等Iterable变成Iterator可以使用iter()函数
    4. iter([])
    5. Iterator对象表示的是一个数据流

