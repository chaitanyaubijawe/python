import threading
import time
counter = 1
lock = threading.Lock()
# this should be used when working on local method parameters....
#lock = threading.RLock()

def m1():

    print("Accessing m1 : ", threading.current_thread().name)
    # lock.acquire()
    for i in range(20):
        print(" Thread working is :: ", threading.current_thread().name)
        #time.sleep(1)
        #m2()
        global counter
        counter += 1
    # lock.release()
    print("Releasing m1 : ", threading.current_thread().name)

def m2():
    print("This is common method. Should be accessed by single thread at a time.",  threading.current_thread().name)


threads_list = []
for i in range(10000):

    nimesh = threading.Thread(target=m1, args=(), name="Thread-" + str(i), )
    threads_list.append(nimesh)

for t in threads_list:
    t.start()



for t in threads_list:
    t.join()


print("Counter :: ", counter)