
# from module_1 import m1
# from module_1 import *
import module_1 as mod_1

def m2():
    print("Inside module 2....")
    mod_1.m1()

m2()

print("__name__ of module_2.py is :: " + __name__)
