from threading import Thread
from multiprocessing import Process,Pool
import time

def fun():
    time.sleep(3)
    a=1
    b=2
    c=3
    sum=a+b+c
    return sum

#通过复写Thread类,自定义一个get_result()方法，获取函数的结果
class myThread(Thread):
    def __init__(self,func,kwargs):
        super(myThread,self).__init__()
        self.func = func
        self.kwargs = kwargs

    def run(self):
        self.result =self.func(**self.kwargs)

    def get_result(self):
        try:
            return self.result
        except:
            return None

def multiThreadMain():
    stime = time.time()
    tl = []
    for _ in range(5):
        tl.append(myThread(fun, kwargs={}))
    for t in tl:
        t.start()
    for t in tl:
        t.join()                #指定 thread 线程优先执行完毕
        print(t.get_result())   #获取函数结果
    etime = time.time()
    print("多线程：Total ", etime-stime, " s")

def multProcessMain():
    stime = time.time()
    p = Pool(5)
    for _ in range(5):
        p.apply_async(fun,args=())
    p.close()
    p.join()
    etime = time.time()
    print("多进程：", etime-stime, "s")

def iterMain():
    stime = time.time()
    for _ in range(5):
        fun()
    etime = time.time()
    print("普通循环：", etime-stime, "s")


#多线程传参示例
class test_thread():
    def __init__(self):
        self.a = 10
        self.b = 15
        self.c = 20

    def do_it(self):
        sum = []
        for h in range(2):
            thread_list = []
            for i in range(5):
                def do_test(number):
                    print(number)
                    time.sleep(3)
                    if self.a == 20 or self.c == 20:
                        sum.append('a')
                    else:
                        sum.append('b')

                thread_list.append(myThread(do_test,kwargs={'number': i}))

            for t in thread_list:
                t.start()

            for t in thread_list:
                t.join()

        return sum

if __name__ == '__main__':
    multiThreadMain()
    # multProcessMain()
    # iterMain()
    d=test_thread()
    print(d.do_it())
