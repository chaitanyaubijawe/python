
# import modules.module_one as one
# import session_3.modules.module_one as one
# import module_one as one


# one.m1_module_1()


import sys

print("before..")
print(sys.path)
print(type(sys.path))

sys.path.append("/Users/chaitanya/CB/python_training/python-sessions/batch_5/")
print("After..")
print(sys.path)


# import module_one as one
import session_3.modules.module_one as one


one.m1_module_1()
print(one.var)

def m12():
    # print("First")
    a = 5
    b = 5
    sum = a + b
    return sum



def m123(arg):
    print("Second.....")
    result = arg()
    print(result)


print(m12)

m123(m12)


print("-----------------")


def m4():
    print("M4")

def m5():
    return m4

r = m5()
r()


def m6():
    def m7():
        print("m7")
    def m8():
        print("m8")

    m8()
    m7()
    # m6()
m6()
