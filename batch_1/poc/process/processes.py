import multiprocessing
import time
import os
counter = 0

def m1():
    print("Here inside process:: ", multiprocessing.current_process().name)
    # lock.acquire()
    for i in range(20):
        print("Working inside process:: ", multiprocessing.current_process().name, os.getpid(), os.getppid())
        time.sleep(1)
        #m2()
        global counter
        counter += 1
    print("Working inside process:: ", multiprocessing.current_process().name, os.getpid(), os.getppid(), counter)
    # lock.release()




p1 = multiprocessing.Process(target=m1, name="p1")
p2 = multiprocessing.Process(target=m1, name="p2")

p1.start()
p2.start()
p2.join()
p2.join()