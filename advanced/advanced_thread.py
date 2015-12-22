#python多线程
#两种方式使用线程：函数或者类来包装线程对象
#函数式 thread.start_new_thread(function, args[, kwargs])
import threading
import time

class mThread(threading.Thread):
        def __init__(self, threadID, name, counter):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name;
                self.counter = counter
        def run(self):
                while 1:
                        time.sleep(1)
                        print("ThreadName is ", self.name,time.ctime(time.time()),end='\n')
                

t1 = mThread(1, "Thread-1", 1)
t2 = mThread(2, "Thread-2", 2)

t1.start()
t2.start()

