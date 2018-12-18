l = [1,2]

# what is the top most parent of Exception class...
try:
    print("print element at index  3... " + str(l[3]))
    # print("print element at index  3... ")
# handling a very specific exception
except NameError as ie:
    print("Handling NameError here... " + str(ie))
except IndexError as ie:
    print("Handling IndexError here... " + str(ie))
except Exception as e:
    print("Handling generic Exception here... " + str(e))

else:
    print("this is else block will be executed if exception is not raised....")
finally:
    print("this is clean up section.... Will be execute always...")


print("print random....%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


def m():
    # what is the top most parent of Exception class...
    try:
        return
        # break
        # continue
        print("M: :::print element at index  3... " + str(l[3]))

    except Exception as e:
        print("M: :::Handling generic Exception here... " + str(e))
    else:
        print("M: :::this is else block will be executed if exception is not raised....")
    finally:
        print("M: :::this is clean up section.... Will be execute always...")


m()

print("here......")


# exercises:

#1. make use of for loop with break and continue...  inside try except and outside try except....
#1. make use of for loop with break and continue...  inside try except and outside try except.... and from within try raise your exception
