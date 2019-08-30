# Python基础
### 知识点总结

> * 数据类型和变量

     1. r''
     2. '''...'''
     3. True、False
     4. and、or和not
     5. None
     6. 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
     7. 变量本身类型不固定的语言称之为动态语言(a = 123  a = 'ABC')，与之对应的是静态语言(例如Java:int a = 123;a = "ABC"; // 错误)。
     8. 在Python中，通常用全部大写的变量名表示常量：PI = 3.14159265359
     9. /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：9 / 3=3.0
     10. 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：10 // 3=3
     11. 余数运算，可以得到两个整数相除的余数：10 % 3=1

> * 字符串和编码

     1. ASCII编码：127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码。
     2. Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
     3. ASCII编码是1个字节，而Unicode编码通常是2个字节。
     4. 把Unicode编码转化为“可变长编码”的UTF-8编码。
     5. Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
     6. ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
     7. 十六进制的str：'\u4e2d\u6587'=='中文'
     8. bytes类型的数据用带b前缀的单引号或双引号表示：
     9. str通过encode()方法可以编码为指定的bytes
     10. 把bytes变为str，就需要用decode()方法。传入errors='ignore'忽略错误的字节
     11. str包含多少个字符，可以用len()函数
     12. 计算bytes字节数，也可以用len()
     13. 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
     14. %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

> * 使用list和tuple

     1. list = ['Michael', 'Bob', 'Tracy']
        #list是一种有序的集合，可以随时添加和删除其中的元素。
     2. len(list)
     3. list[-1]
     4. list.append()
     5. list.insert()
     6. list.pop()
     7. list[1] = 'Sarah'
     8. tuple = ('Michael', 'Bob', 'Tracy')
        #tuple:一旦初始化就不能修改
     9. 只有1个元素的tuple：t = (1,)

> * 条件判断

     1. elif是else if的缩写
     2. str=input()

> * 循环

    1. for...in
    2. range(101)就可以生成0-100的整数序列
    3. list(range(5))
    4. while
    5. break可以提前退出循环
    6. continue跳过当前的这次循环，直接开始下一次循环

> * 使用dict和set

    1. 字典：dict的支持，dict全称dictionary
    2. d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    3. d['Michael']
    4. d['Michael'] = 35
    5. 'Michael' in d
    6. d.get('Thomas', -1)
    7. d.pop('Bob')
    8. set1 = set([1, 2, 3])
    9. set1.add(4)
    10. set1.remove(4)
    11. set1 & set2
    12. set1 | set2
    13. ['c', 'b', 'a'].sort()
