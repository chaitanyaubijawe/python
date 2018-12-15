#from module_1 import m1
#from module_1 import *

import module_1

def m2():
    print("This is m2 from module 2....")
    #module_1.m1()



if __name__ == "__main__":
    m2()
    print("__name__ in module_2.py:: " + __name__)
