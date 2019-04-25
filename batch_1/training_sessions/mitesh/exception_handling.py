print("Hi there 1")
a = 3
try:
    a = 5/0
    # try:
    #     s = a + "asdas"
    # except Exception as e:
    #     print("Here...... Exception "+ str(e))
    # finally:
    #     print("finally inside...")
except ZeroDivisionError as zex:
    print("Hey you got ZeroDivisionError while processing... " + str(zex))
except Exception as ex:
    print("Hey you got Exception while processing... " + str(ex))
else:
    print("This is ELSE block. Will only executed if exception does not occur.")
finally:
    print("Here is finally. This will always be executed.")
print("Hi there 2")
