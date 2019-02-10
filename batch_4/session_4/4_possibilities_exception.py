
print("before....")
try:
    a = 4/0
except Exception as e:
    print("Excption occurs :: " + str(e) + str(e.__dict__))
else:
    print("this is else block... will be executed if exception not occurred...")
finally:
    print("finally")
