import os

print('''---------------------操作文件和目录---------------------
''')

# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
print("操作系统类型:", os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
try:
    print("\n详细的系统信息:")
    os.uname()
except Exception as e:
    print(e)
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# # # # # # # # # # #
# # # # # # # # # # # 环境变量# # # # # # # # # # # # #
# # # # # # # # # # #
#
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print("\n环境变量:", os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print("JAVA_HOME:", os.environ.get('JAVA_HOME'))

# # # # # # # # # # # #
# # # # # # # # # # # 操作文件和目录# # # # # # # # # # # # #
# # # # # # # # # # # #
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
# 查看、创建和删除目录可以这么调用：
print("\n查看当前目录的绝对路径:", os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
newPath = os.path.join(os.path.abspath('.'), 'testdir')
print("一、找到新目录完整路径：", newPath)
# ***然后创建一个目录:
print("\n---------------------不想测试操作文件和目录过程直接用多个回车跳过---------------------")
if input("--------二、创建一个目录？0 or 1--------") == "1":
    try:
        os.mkdir(newPath)
        print("--------创建目录完成,用快捷键alt+tab切换应用程序进行刷新查看结果--------")
    except Exception as e:
        print(e)
# ***删掉一个目录:
if input("\n--------三、删掉一个目录？0 or 1--------") == "1":
    try:
        os.rmdir(newPath)
        print("--------删除目录完成,用快捷键alt+tab切换应用程序进行刷新查看结果--------")
    except Exception as e:
        print(e)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
print("\n使用os.path.join()拼接路径", os.path.join("/Users/michael/testdir", "file.txt"))
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print("使用os.path.split分割路径", os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print(os.path.splitext('/path/to/file.txt'))
# 假定当前目录下有一个test.txt文件：
# ***新建文件:
s = input("\n--------新建文件？0 or 1--------")
if s == "1":
    with open("test.txt", "w") as f:
        print("--------新建完成,用快捷键alt+tab切换应用程序进行刷新查看结果--------")
# ***对文件重命名:
if input("\n--------对文件重命名？0 or 1--------") == "1":
    try:
        os.rename('test.txt', 'test.py')
        print("--------对文件重命名完成,用快捷键alt+tab切换应用程序进行刷新查看结果--------")
    except Exception as e:
        print(e)
# ***删掉文件:
if input("\n--------删掉文件？0 or 1--------") == "1":
    try:
        os.remove('test.py')
        print("--------删掉文件完成,用快捷键alt+tab切换应用程序进行刷新查看结果--------")
    except Exception as e:
        print(e)

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。
# 比如我们要列出当前目录下的所有目录
print("当前目录下的所有目录:", [x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件，也只需一行代码：
print("当前目录下所有的.py文件", [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

ll = []


def getDir(path):
    for x in os.listdir(path):
        if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt':
            path = os.path.realpath(x)
            print(path)
            ll.append(path)
        if os.path.isdir(x):
            getDir(os.path.realpath(x))


getDir(".")
print(ll)
