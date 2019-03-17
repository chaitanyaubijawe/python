## If elif else.....
# break....
# continue...
# return
for item in range(1,10):

    if ( item == 5):
        print("Inside if block....")
        print("Value of item :: " + str(item))
        break
    elif(item > 5):
        print("Value is greater than = 5..")
    else:
        print("Inside else block...")
    # Inside for.....
    print("Everytime print :: value :: " + str(item))

print("------------------------------")
for item in range(1,10):

    if ( item == 5):
        print("Value of item :: " + str(item))
        break
    print("Everytime print :: value :: " + str(item))


print("------------------------------")
for item in range(1,10):

    if ( item == 5):
        print("Value of item :: " + str(item))
        continue
    print("Everytime print :: value :: " + str(item))

def m():
    print("------------------------------")
    for item in range(1,10):

        if ( item == 5):
            print("Value of item :: " + str(item))
            return
        print("Everytime print :: value :: " + str(item))
    print("Exiting method.....")

m()

# while loop.
