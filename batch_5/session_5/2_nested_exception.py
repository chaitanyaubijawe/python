def m():
    a = 10
    try:
        a = 10 / 2
        print("Inside else block...." + str(a))

        try:
            r = a / 0
        except Exception as e:
            print("Nested Exception.......")
        else:
            print("Else:: nested :: ")
        finally:
            print("finally here.... nested...")

    except Exception as ex:
        print("Exception:: " + str(ex))
    else:
        print("Inside else:: ")
    finally:
        print("finally block of code...")

m()
