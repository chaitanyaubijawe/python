import multiprocessing


import time



def m1(arg):

    l = []
    for i in range(30):
        print("Inside Process :: " +multiprocessing.current_process().name + " -- arg -- " + arg + " --- " + str(i) + " id :: " + str(multiprocessing.current_process().pid))
        l.append(i)

        if(i >= 15 and multiprocessing.current_process().name == "Mahindra"):
            break
        time.sleep(1)

    print("Inside Process :: " +multiprocessing.current_process().name + " List :: " + str(l))



p1 = multiprocessing.Process(target=m1, name="Mahindra", args=("Nikam",))
p2 = multiprocessing.Process(target=m1, name="Chaitanya", args=("Bijawe",))

p1.start()
p2.start()

p1.join()
p2.join()