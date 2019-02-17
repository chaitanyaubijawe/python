

import threading
import time

lock = threading.Lock()
[]
def m1(arg):
    lock.acquire()
    for i in range(10):
        print("Inside thread :: " +threading.current_thread().name + " -- arg -- " + arg + " --- " + str(i))
        time.sleep(1)
    lock.release()




t1 = threading.Thread(target=m1, name="Mahindra", args=("Nikam",))
t2 = threading.Thread(target=m1, name="Chaitanya", args=("Bijawe",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread dies here...")





