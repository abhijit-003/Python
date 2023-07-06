#multithreading semaphore

from threading import *
import time
obj = Semaphore(3)
def msg(name):
    obj.acquire()

    for i in range(5):
         print('Hello=',i, end = ' ')
         time.sleep(1)
         print(name)
         obj.release()

t1 = Thread(target=msg,args=("Thread 1",))
t2 = Thread(target=msg,args=("Thread 2",))
t3 = Thread(target=msg,args=("Thread 3",))
t4 = Thread(target=msg,args=("Thread 4",))
t5 = Thread(target=msg,args=("Thread 5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()