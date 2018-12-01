a = 1
b = 2

add = a + b

print("Addition is :: " + str(add))

a = 3
b = 4

add = a + b

print("Addition is :: " + str(add))


def addition(a, b):
    add = a + b
    print("Addition is : ", add)


addition(a, b)

a = 5
b = 7

addition(a, b)
addition(33, 55)


# m1()
# first

def m1():
    print("Inside m1")


# calling of a function
m1()


# second
def m2(arg1, arg2):
    print("Function with two argument ", arg1, arg2)


m2(arg1=1, arg2=2)

a = 1
b = 3

m2(a, b)


# second

def m3(arg1):
    z = 23
    print("Single argument, ", arg1)


a = 2
m3(a)


def m4(arg1, arg2=None, arg3=None):
    print("Single argument, ", arg1)
    if arg2 is not None:
        print("second default argument", arg2)
    if arg3 is not None:
        print("third default argument", arg3)


m4(3)
m4(arg1=3)
m4(arg1=3, arg2=4, arg3=5)
m4(arg1=3, arg2=4, arg3=5)


# forth
def m5(arg=None):
    print("Default argument function...")
    if arg is not None:
        print("Default argument function... called with argument : ", arg)


m5(arg=2)
m5()
m5(5)
m5("Mitesh")


def m6():
    pass


m6()
