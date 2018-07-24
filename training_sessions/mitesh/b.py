print ("hi  b.py")
#import a
#greeting2_from_a = a.greeting2
#a.m1()

#from a import m1, greeting
from a import *

greeting_from_a = greeting
greeting2_from_a = greeting2

print(greeting_from_a, greeting2_from_a)

m1()



import sys

print(sys.path)
