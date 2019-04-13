class Shivam(Exception):

    def __init__(self, msg):
        super().__init__()# Exception class constructor...
        self.msg = msg
        print("Constructor is called")

    def __str__(self):
        return str(self.msg)




def m():
    a = 10
    try:

        # Shivam("My Exception has occured....")
        # raise Shivam("My Exception has occured....")
        a = 10 / 2
        print("Inside else block...." + str(a))
        r = a / 0

        # for break
        # for continue
    except Shivam as sex:
        print("Shivam:: " + str(sex))
    except ZeroDivisionError as zex:
        print("ZeroDivisionError:: " + str(zex))
    except Exception as ex:
        print("Exception:: " + str(ex))
    else:
        print(a)
    finally:
        print("finally block of code...")

m()

# return
# What will happen if we write return in try block.
# nested try except
