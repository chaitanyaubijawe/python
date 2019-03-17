def m():
    print("inside m")

if __name__ == "__main__":
    print(" TWO.Py :: Name of current module is -- " + __name__)
    m()
else:
    print("Inside else... this is not a main module...."  + __name__)
