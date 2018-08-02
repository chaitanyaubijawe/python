def m1():
    print("inside m1.")


def m2(arg):
    print("inside m2", arg)


def m3(arg=5):
    print("inside m3. Default value arg ", arg)


def m4(arg1=5, arg2=6):
    print("inside m4. Default value arg1 and arg2", arg1, arg2)


def mlast(*p):
    print(p)
    print(type(p))


m1()
m2("asd")
m2(4)
m3()  # without value called.
m3("string is passed")
m3(55)
m3(arg="string is passed")
m3(arg=4)
