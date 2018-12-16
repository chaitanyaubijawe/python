a = 51
b = 4
add = a + b
logMessage = "Addition is : "
print( logMessage + str(add))


i2 = 44
i3 = 55


add = i2 + i3

print(logMessage + str(add))


def abhishek(a, b):
    return a + b


print(logMessage + str(abhishek(a=1,b=2)))
print(logMessage + str(abhishek(10,20)))
print(logMessage + str(abhishek(1022,2011)))



def m():
    print("This is simple function....")

m()

def m2():
    print("This is simple function...." )

m2()

def m2(arg):
    print("This is simple function...." + str(arg))

# m2()
m2(10)
m2([1,2,3])
m2({"a":"A"})


def m3(arg,ar,ZSD,asd):
    print("This is simple function...." + str(arg))


def m3(arg_1="DEFAULT"):
    print("This is simple function...." + str(arg_1))


m3()
m3("provided value")




def m4(arg_1="DEFAULT", arg_2="DEFAULT"):
    print("This is simple function...." + str(arg_1))

m4()
m4(arg_1="10")
m4(arg_2="100")
m4(arg_1="100",arg_2="100")

def m5(*args):
    print("Argumnets are " + str(args))
    print(args[0])
    print(type(args))


m5(1,123,"asdadds", 123132, "asdasdaadsasda")




def m6(**kwargs):
    print("Argumnets are " + str(kwargs))

    print(kwargs["abhishek"])
    print(type(kwargs))


m6(abhishek=25,chaitanya=29,onkar=33)


# exercise create calculator methods
# add(a,b)
# add(a,b,c)
# subtract()




# return

op = print("laksflakjsd")

print(type(op))

op1 = None

print(type(op1))
print("#################")





def add(a,b):
    return a + b
#
op = add(1,2)
print(type(op))
print(op)




def m7():
    # return []
    # return ()
    # return {}
    # return 2
    # return "string"
    return True


def m8(arg):

    if(arg == 1):
        return  True
    else:
        return False
        # below line of code will not executed...
        print("this is false.....")


result = m8(2)

print(result)


def m10():
    print("m10 function")

def m9():
    ## returning afunction within a function
    return m10


m9() ## return type is function....
print(type(m9()))
m9()()
