import threading
import time

print('''---------------------多线程---------------------
''')


# # # # # # # # # # #
# # # # # # # # # # # Thread # # # # # # # # # # # # #
# # # # # # # # # # #

# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
#
# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，
# Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
#
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。

# *********启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。

# # # # # # # # # # #
# # # # # # # # # # # Lock # # # # # # # # # # # # #
# # # # # # # # # # #
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：
# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print("\n多线程操作balance=", balance)
# 由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
# 但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

# 如果我们要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，
# 直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
# 坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，
# 效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，
# 可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

# 小结
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# 
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。