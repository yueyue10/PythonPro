# 错误、调试和测试
### 知识点总结

> * 错误处理

     1. try...except...finally...
     2. Python的错误其实也是class，所有的错误类型都继承自BaseException，
        所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
     3. 调用栈
     4. 记录错误
     5. logging
     6. 抛出错误
        # err_raise.py
        class FooError(ValueError):
            pass

        def foo(s):
            n = int(s)
            if n==0:
                raise FooError('invalid value: %s' % s)
            return 10 / n

        foo('0')

> * 调试

     1. 断言
        assert
     2. 启动Python解释器时可以用-O参数来关闭assert：
        python -O err.py
        断言的开关“-O”是英文大写字母O，不是数字0。
     3. logging
        logging.basicConfig(level=logging.INFO)
     4. pdb
        以参数-m pdb启动
        输入命令l来查看代码
        输入命令n可以单步执行代码：
        任何时候都可以输入命令p 变量名来查看变量：
        输入命令q结束调试，退出程序：
     5. pdb.set_trace()
        在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
        运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
     6. IDE
     7. 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

> * 单元测试

     1. TDD
        Test-Driven Development
        测试驱动开发
     2. 比如对函数abs()
        我们可以编写出以下几个测试用例：
            输入正数，比如1、1.2、0.99，期待返回值与输入相同；
            输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
            输入0，期待返回0；
            输入非数值类型，比如None、[]、{}，期待抛出TypeError。
     3. 单元测试
        class TestDict(unittest.TestCase):

            def test_init(self):
                d = Dict(a=1, b='test')
                self.assertEqual(d.a, 1)
                self.assertEqual(d.b, 'test')
                self.assertTrue(isinstance(d, dict))
        1. 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
        2. 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        3. 对每一类测试都需要编写一个test_xxx()方法，我们可以用unittest.TestCase提供了很多内置的条件判断输出是否是我们所期望的
            1.  assertEqual()：
            2.  通过d['empty']访问不存在的key时，断言会抛出KeyError：
                 with self.assertRaises(KeyError):
                    value = d['empty']
            3.  d.empty访问不存在的key时，我们期待抛出AttributeError：
                 with self.assertRaises(AttributeError):
                    value = d.empty
     4. 运行单元测试
        最简单的运行方式是在mydict_test.py的最后加上两行代码：
            if __name__ == '__main__':
                unittest.main()
            这样就可以把mydict_test.py当做正常的python脚本运行：
            $ python mydict_test.py
        另一种方法是在命令行通过参数-m unittest直接运行单元测试：
            $ python -m unittest mydict_test
     5. setUp与tearDown
        这两个方法会分别在每调用一个测试方法的前后分别被执行。

> * 文档测试

    1. doctest
        '''
            Simple dict but also support access as x.y style.

            >>> d1 = Dict()
            >>> d1['x'] = 100
            >>> d1.x
            100
            >>> d1.y = 200
            >>> d1['y']
            200
            >>> d2 = Dict(a=1, b=2, c='3')
            >>> d2.c
            '3'
            >>> d2['empty']
            Traceback (most recent call last):
                ...
            KeyError: 'empty'
            >>> d2.empty
            Traceback (most recent call last):
                ...
            AttributeError: 'Dict' object has no attribute 'empty'
            '''