l = [1,2]
try:
    print(l[3])
except Exception as e:
    print("Error :: " + str(e))
    # terminate program
    # raise Exception..
    # continue with some default....
