a = 1
b = 3

sum = a + b

print(sum)

# dynamic typing in python....

a = 3
b = 5

sum = a + b

print(sum)


# FUNCTIONS/methods

def m():
    print("hello within a function/method.")


m()


def m1():
    a = 1
    b = 2
    print(a + b)

m1()

print("#####")
def m2(arg_1, arg_2):
    a = arg_1
    b = arg_2
    print(a + b)

m2(1,2)
m2(1,5)
m2(1,6)

print("#####")
def m3(arg_1=0, arg_2=4):
    a = arg_1
    b = arg_2
    print(a + b)
m3()
m3(2,3)
m3(2)
m3(arg_1=2, arg_2=5)
m3(arg_2=5)

print("#####")
def m4(arg_1=None):
    print(arg_1)

m4()
m4(arg_1="PASSED VALUE")
m4("ANOTHER VALUE")


print("#####")
def m5(arg_1, arg_2=None):
    print(arg_1)
    print(arg_2)

m5(1)
m5(1, 2)
m5(1, arg_2="ANOTHER VALUE")



print("#####")
# default value followed by non default arg does not work.
# def m6(arg_1=None, arg_2):
#     print(arg_1)
#     print(arg_2)
#
# m6(1)


def m7(arg_1, arg_2, arg_3=None):
    sum = arg_1 + arg_2
    print(sum)

m7(1,2)


# return :
def m8(arg_1, arg_2):
    sum = arg_1 + arg_2
    return sum

result = m8(1,23)

print(result)


def m9(arg_1):
    print(type(arg_1))

l = [1,2,3,4]
m9(1)
m9(l)
m9((1,2,3,4))
m9({"a":"A"})
m9("ABC")


def m10(arg_1,arg_2,arg_3,arg_4):
    print(arg_1)
    print(arg_2)
    print(arg_3)
    print(arg_4)

m10(1,2,3,4)

print("-------variable arguments...-------")
def m11(*args):
    print(type(args))
    sum = 0
    for item in args:
        sum += item
    return sum

print(m11(1,2,3))


print("-------variable arguments...-------")
def m12(**kvargs):
    print(type(kvargs))
    # print(kvargs)
    return kvargs

m12Result = m12(name="ABC",age=20)
print(m12Result)

# this does not work in case of this :: **kvargs.
# d = {"name":"Chaitanya", "Age":30}
# m12Result = m12(d)
# m12Result = m12(1)
# m12Result = m12([1,2,3])
# m12Result = m12(1,2,3)
# print(m12Result)
