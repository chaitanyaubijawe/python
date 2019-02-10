
print("before....")
try:
    a = 4/0
except Exception as e:
    print("Excption occurs :: " + str(e) + str(e.__dict__))

print("after...")
