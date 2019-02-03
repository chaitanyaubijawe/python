
def m1():
    print("Inside m1 of module_1 one.py")
    print("ONE.py :: __name__ :: " + __name__)

def m2():
    print("hey there this is getting executed every time ;(")


if __name__ == "__main__":
    print("hey there this is getting executed every time ;(")
    m2()
