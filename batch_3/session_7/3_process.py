import multiprocessing

import time
import os


def m(arg):

    for i in range(5):
        print("Argument passed is :: " +str(arg)+ " Value of i is :: " + str(i) + " inside process :: " + multiprocessing.current_process().name + " Process ID: " + str(os.getppid()))
        time.sleep(5)




p1 = multiprocessing.Process(target=m, args=(1,), name="firstProcess")
p1.start()
p1.join()

p2 = multiprocessing.Process(target=m, args=(1,), name="SecondProcess")
p2.start()
p2.join()

print("Parent process exiting" + multiprocessing.current_process().name + " Process ID: " + str(os.getppid()))