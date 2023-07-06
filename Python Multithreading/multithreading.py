'''
#using threading
import threading
import time
def msf():
    time.sleep(1)
    for i in range(1,10):
        print(i)

def msg():
    time.sleep(1)
    for i in range(10,15):
        print(i)
t1 = threading.Thread(target=msf())
t2 = threading.Thread(target=msg())


t1.start()

t2.start()
t1.join() #wait till one thread executed completelys
'''

#2 using _thread
import _thread
import time

def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i)
        time.sleep(1)  # Sleep for 1 second between numbers

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Thread 2:", letter)
        time.sleep(1)  # Sleep for 1 second between letters

# Create threads and specify target functions
thread1 = _thread.start_new_thread(print_numbers, ())
thread2 = _thread.start_new_thread(print_letters, ())

time.sleep(6)  # Sleep for enough time to allow threads to finish

print("Program completed.")

