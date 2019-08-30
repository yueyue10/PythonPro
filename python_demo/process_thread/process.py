import os
from multiprocessing import Process

print('''---------------------多进程---------------------
''')

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
try:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
except Exception as e:
    print(e)


# 运行结果如下：
#
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.
#
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。
# 由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！

# # # # # # # # # # #
# # # # # # # # # # # multiprocessing # # # # # # # # # # # # #
# # # # # # # # # # #
# 由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


print("\n")
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


