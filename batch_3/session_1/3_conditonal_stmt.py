

flag = False

result = not flag

print(result)
# if (<boolean expression..>):
#     #do things here.
# elif(<boolean expression..>):
#     # another things to be done here.
# else:
#     # if not matched above any criteria..


if(flag):
    print("The value of flag is true.....")
elif(not flag):
    print("The value of flag is false....")
else:
    print("The valus is neither false nor true....")


flag = "Abhisheklll"
flag = "Abhishek"
flag = "Chaitanya"


if(flag == "Chaitanya"):
    print("The value of flag is Chaitanya.....")
elif(flag == "Abhishek"):
    print("The value of flag is flag = Abhishek")
else:
    print("The valus is neither Chaitanya nor Abhishek....")


# break continue and return


def m():
    for i in range(1,11):
        print("Value of i is:: " +str(i))
    print("For loop ends::: ")

m()

print("######################")

def m2():
    for i in range(1,11):
        if(i == 8 ):
            break
        print("Value of i is:: " +str(i))
    ##############loop ends here#############
    print("For loop ends::: ")

m2()


print("######################")

def m3():
    for i in range(1,11):
        if(i == 8):
            continue
        print("Value of i is:: " +str(i))
    ##############loop ends here#############
    print("For loop ends::: ")

m3()


print("######################")

def m4():
    for i in range(1,11):
        if(i == 8):
            return
        print("Value of i is:: " +str(i))
    ##############loop ends here#############
    print("For loop ends::: ")

m4()
