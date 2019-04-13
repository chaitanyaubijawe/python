a = 10
try:
    a = 10 / 2
    print("Inside Try block...." + str(a))
    r = a / 0
except ZeroDivisionError as zex:
    print("ZeroDivisionError:: " + str(zex))
except Exception as ex:
    print("Exception:: " + str(ex))
else:
    print(a)
finally:
    print("finally block of code...")
