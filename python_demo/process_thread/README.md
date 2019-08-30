# 进程和线程
### 知识点总结

> * 多进程

     1. fork可以在Python程序中轻松创建子进程：
        # Only works on Unix/Linux/Mac:
     2. multiprocessing Process
        # 子进程要执行的代码
        def run_proc(name):
            print('Run child process %s (%s)...' % (name, os.getpid()))

        if __name__=='__main__':
            print('Parent process %s.' % os.getpid())
            p = Process(target=run_proc, args=('test',))
            print('Child process will start.')
            p.start()
            p.join()
            print('Child process end.')
        执行结果如下：

        Parent process 928.
        Process will start.
        Run child process test (929)...
        Process end.
        创建子进程时，只需要传入一个执行函数和函数的参数，
        创建一个Process实例，用start()方法启动。
        join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
     3. Pool
        def long_time_task(name):
            print('Run task %s (%s)...' % (name, os.getpid()))
            start = time.time()
            time.sleep(random.random() * 3)
            end = time.time()
            print('Task %s runs %0.2f seconds.' % (name, (end - start)))

        if __name__=='__main__':
            print('Parent process %s.' % os.getpid())
            p = Pool(4)
            for i in range(5):
                p.apply_async(long_time_task, args=(i,))
            print('Waiting for all subprocesses done...')
            p.close()
            p.join()
            print('All subprocesses done.')

        执行结果如下：
        Parent process 669.
        Waiting for all subprocesses done...
        Run task 0 (671)...
        Run task 1 (672)...
        Run task 2 (673)...
        Run task 3 (674)...
        Task 2 runs 0.14 seconds.
        Run task 4 (673)...
        Task 1 runs 0.27 seconds.
        Task 3 runs 0.86 seconds.
        Task 0 runs 1.41 seconds.
        Task 4 runs 1.91 seconds.
        All subprocesses done.
        对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
     4. subprocess
        在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
        print('$ nslookup www.python.org')
        r = subprocess.call(['nslookup', 'www.python.org'])
        print('Exit code:', r)

        运行结果：
        $ nslookup www.python.org
        Server:		192.168.19.4
        Address:	192.168.19.4#53
     5. communicate()
     6. 进程间通信：Queue Pipes

> * 多线程

     1. Python的线程是真正的Posix Thread，而不是模拟出来的线程。
        Python的标准库提供了两个模块：_thread是低级模块，threading是高级模块.
     2. 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
        # 新线程执行的代码:
        def loop():
            pass
        t = threading.Thread(target=loop, name='LoopThread')
        t.start()
        t.join()
     3. Lock
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

> * ThreadLocal

     1. 一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，
        不会影响其他线程，而全局变量的修改必须加锁。
     2. ThreadLocal
        # 创建全局ThreadLocal对象:
        local_school = threading.local()

        def process_student():
            # 获取当前线程关联的student:
            std = local_school.student
            print('Hello, %s (in %s)' % (std, threading.current_thread().name))

        def process_thread(name):
            # 绑定ThreadLocal的student:
            local_school.student = name
            process_student()

        t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
        t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        执行结果：

        Hello, Alice (in Thread-A)
        Hello, Bob (in Thread-B)

> * 进程 vs. 线程

     1. 要实现多任务，通常我们会设计Master-Worker模式，
        Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

> * 分布式进程

    1. 在Thread和Process中，应当优选Process，因为Process更稳定，
        而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
    2. managers QueueManager
