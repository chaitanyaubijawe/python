import threading
import time

lock = threading.Lock()


def m(arg):
    print("Entering :: inside m in thread :: " + threading.current_thread().name)
    lock.acquire()
    for i in range(4):
        print("Argument passed is :: " +str(arg)+ " Value of i is :: " + str(i) + " inside thread :: " + threading.current_thread().name)
        time.sleep(1)
    lock.release()
    print("Exiting :: inside m in thread :: " + threading.current_thread().name)

t1 = threading.Thread(target=m, args=(1,), name="firstThread")
t2 = threading.Thread(target=m, args=(2,), name="SecondThread")


t1.start()
t2.start()

t2.join()
t1.join()