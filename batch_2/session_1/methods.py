def m():
    print("normal m method.....")

m()

print(m)

def m2(arg_1):
    print("normal m method....." + str(arg_1))


m2(1)
m2("asfasdas")
m2(["1", "2"])
m2({"1":"zsfasd", "2":"asdasd"})


def m3(arg_1,arg_2):
    print("normal m method....." + str(arg_1) + str(arg_2))


m3("1", "111")


def m4(arg_1="0", arg_2="DEFAULT"):
    print("normal m method....." + str(arg_1) + str(arg_2))


m4()
m4("Paassed value....")
m4(arg_1= [1,2,34])
m4(arg_2= "Paassed value....")
m4(arg_1= "Paassed value....", arg_2="asfsdas")


def m5(*args):
    print(type(args))
    print(args)


m5("person name",2,3,4,5,6,234,234,234,234)
m5("person name","last name")


def m6(**kwargs):
    print(type(kwargs))
    print(kwargs)

v = 123123
m6(key="123", key_2="asdfasd")



def m7():
    # return {}
    # return []
    # return ()
    # return ""
    return 3

def m8():
    def m9():
        return "anything...."

    return m9

m8()()


def m10():
    return m7()

print(type(m10()))

print(m10())
