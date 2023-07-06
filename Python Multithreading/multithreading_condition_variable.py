#multithreading_condition_variable.py
import threading
shared_data = []

#instance of condiotion variable
condition = threading.Condition()

def producer():
    global shared_data

    with condition:
        shared_data.append("new data")

        condition.notify()

def consumer():

    global shared_data

    with condition:
        while not shared_data: #chek the condition 
            condition.wait() # and wait till the condition not satisified
        
        data = shared_data.pop()
        print("data= ",data)


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()