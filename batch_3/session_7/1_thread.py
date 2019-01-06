import threading
import time


def m(arg):

    for i in range(4):
        print("Argument passed is :: " +str(arg)+ " Value of i is :: " + str(i) + " inside thread :: " + threading.current_thread().name)
        time.sleep(1)





# m()
#

t1 = threading.Thread(target=m, args=(1,), name="firstThread")
t2 = threading.Thread(target=m, args=(2,), name="SecondThread")


t1.start()
t2.start()

t2.join()
t1.join()


print("this is main thread:: exiting:: " + threading.current_thread().name)