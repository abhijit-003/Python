import threading

# Create a semaphore with a maximum of 3 permits
semaphore = threading.Semaphore(3)

def worker_thread(worker_id):
    print(f"Worker {worker_id} is trying to acquire the semaphore.")
    semaphore.acquire()
    print(f"Worker {worker_id} acquired the semaphore.")
    
    try:
        # Access the shared resource
        print(f"Worker {worker_id} is accessing the shared resource.")
    
    finally:
        # Release the semaphore
        semaphore.release()
        print(f"Worker {worker_id} released the semaphore.")

# Create worker threads
threads = []
for i in range(1, 6):
    thread = threading.Thread(target=worker_thread, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All worker threads have finished.")
