class A:
    # variable in python
    var_a = 5
    var_b = 5

a = A()

print(a.var_a)
print(a.var_b)

a.var_a = 10
a.var_b = 10

print(a.var_a)
print(a.var_b)
print("---------------------")


class Duster:
    count=0
    # handle= ""
    def __init__(self, args_1, args_2):
        print("Inside constructor...." + str(type(self)))
        self.handle = args_1
        self.clothe = args_2
        # self.count = 0
        Duster.count +=1
    



duster = Duster("Handle", "Clothe")

print(duster.handle)
print(duster.clothe)
print("Count of object " + str(duster.count))



duster2 = Duster("Red Handle2", "White Clothe")
duster3 = Duster("Red Handle3", "White Clothe")
duster4 = Duster("Red Handle4", "White Clothe")
print(duster2.handle)
print(duster2.clothe)
print("Count of object " + str(duster.count))
print("Count of object " + str(duster2.count))
print("Count of object " + str(duster3.count))
print("Count of object " + str(duster4.count))
print(duster2.handle)
print(duster.handle)
