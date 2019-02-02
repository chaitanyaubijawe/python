add  = 1 + 2
print(add)

add  = 3 + 5
print(add)


# def is keyword
# m : is method NAME
# () : are must to have.
def m_1():
    add = 1 + 2
    print(add)

m_1()


def m_2(arg_1, arg_2):
    add = arg_1 + arg_2
    print(add)

m_2(1,23)
m_2(22,22)
m_2(2,4)



def m_3(arg_1=0, arg_2=0):
    add = arg_1 + arg_2
    print(add)



m_3()
m_3(arg_1=1)
m_3(arg_2=1)
m_3(arg_1=1, arg_2=2)


# Non default should come first.
def m_4(arg_1, arg_2=0):
    add = arg_1 + arg_2
    print(add)

m_4(1)



def m_5(arg_1, arg_2, arg_3,arg_4):
    add = arg_1 + arg_2
    print(add)

m_5(1,1,2,3)

print("%%%%%%%%%%%%%")
def m_6(*args):
    print(args[0])
    print(type(args))

m_6(1,1,2,3)


print("%%%%%%%%%%%%%")
def m_7(arg_1=0, arg_2=0, arg_3=0,arg_4=0):
    print(arg_4)
    # print(type())

m_7(arg_1=1,arg_2=1,arg_3=2,arg_4={"asd":"asd"})

print("%%%%%%%%%%%%%")
def m_8(**kargs):
    print(kargs)
    print(type(kargs))

m_8(arg_one=1,arg_2=1,arg_three=2,chaitanya="bijawe")
