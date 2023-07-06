#multithreadin_lock.py

import threading as th
import time
counter = 0

#create instance of Lock
#lock = th.Lock() 
def increase(by):
    global counter
    #lock.acquire()

    local_counter = counter
    local_counter += by

    time.sleep(0.5)

    counter = local_counter
    print(counter)
    
    #lock.release()

t1 = th.Thread(target=increase,args=(10,))
t2 = th.Thread(target=increase,args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()
print("final counter=",counter)
print("completed")
