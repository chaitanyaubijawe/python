
print("before....")
try:
    a = 4/2
except Exception as e:
    print("Excption occurs :: " + str(e) + str(e.__dict__))
finally:
    print("here.... this is finally...... Will be executed every time. meaning  if exception is raised or not raised..")
print("after...")
