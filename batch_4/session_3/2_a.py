class A:
    v1 = "Mahindra"

    def __init__(self, arg_1, arg_2):
        # print("This is constructor......" + str(arg_1) + str(arg_2))
        # self.m1()
        self.instance_arg_1 = arg_1
        self.instance_arg_2 = arg_2

    def m1(self):
        print("Inside M1 it is a instance method....." + str(self.instance_arg_1))
        self.m2()

    def m2(self):
        print("Inside M2 it is a instance method....." + str(self.instance_arg_2) + str(self.v1))

    @classmethod
    def m3(cls):
        print("This is class Method... M3 " + str(cls) + str(cls.v1))


#Dont use this pattern...
    def m4(cls):
        print("This is class Method... M4 " + str(cls) + str(cls.v1))

    @staticmethod
    def m5(arg):

        print("This is static method.,... ")

if __name__ == "__main__":


    a1 = A("1", "OBJECT1....")  # instantiation......
    # object creation.
    #a == > reference variable.

    # print(type(a))
    # a1.m1()
    a1.m2()
    # print(a.v1)
    # A.m3()
    # A.m4(A)
    # print(A.v1)

    a2 = A("1", "OBJECT222222....")

    a2.m2()
    a2.instance_arg_2 = "this is updatedddd....."
    a2.m2()
    a1.m2()

    print(a1.v1)
    print(a2.v1)

    A.v1= "Chaitanya"

    print(a1.v1)
    print(a2.v1)


    A.m5("asfasdasd")
