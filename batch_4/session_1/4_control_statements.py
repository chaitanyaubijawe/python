# controll statements


# return


def m(arg_1, arg_2):
    # add = arg_1 + arg_2
    return arg_1 + arg_2
    # return add

m(1,2)

print(m(1,2))

addition = m(1,2)

print(addition)


def m_2(arg_1, arg_2):
    add = arg_1 + arg_2
    # not returning anything


m_2(1,2)
print(m_2(1,2))


def m_3():
    # add = arg_1 + arg_2
    d = {}
    return d
    # return {}
    # return []
    # return ()
    # return "abcd"
    # return 1
    # return add


def m_4():
    # add = arg_1 + arg_2
    print("hello : this is function returning function....")
    # return None

def m_5():
    # add = arg_1 + arg_2
    return m_4



m4 = m_5()

print(type(m4))

m4()
m_5()()



#Break continue and if elif
for item in range(5):
    if(item == 3):
        break
    print(item)

print("after break.... for loop ends...")



#Break continue and if elif
for item in range(5):
    if(item == 3):
        continue
    print(item)

print("after continue.... for loop does not ends ...")


def m():
    #Break continue and if elif
    for item in range(5):
        if(item == 3):
            return
        print( "Inside for and methiod for return :: "+ str(item))
    print("hello... after return......")

print("after return.... for loop ends overall things ends......")
m()



def m_22():
    #Break continue and if elif
    for item in range(5):
        if(item == 3):
            break
        print( "Inside for and methiod for return :: "+ str(item))
    print("hello... after break......")

print("after return.... for loop ends overall things ends......")
m_22()



def m_33():
    #Break continue and if elif
    for item in range(5):
        print( "Inside for and methiod for return :: "+ str(item))
    # break
    # continue
    print("hello... after break......")
m_33()

print("$$$$$$$$$$$$$$$$$$$$$")

a = 4
if(a == 1):
    print("One")
elif( a== 2):
    print("Two")
else:
    print("nothing..")
