nexclass A:
    count = 0
    def __init__(self):
        print("Inside constructor....")
        A.count +=1

    def m1( self, args_1):
        ''' Instance method...... '''
        self.m1_2()
        print("Inside method m1...."+str(args_1))
        # A.m2()

    def m1_2( self):
        ''' Instance method...... '''
        print("Inside method m1. second version.......")
        print(A.m4(5))

    @classmethod
    def m2(cls):
        ''' Class method...... '''
        print("Inside method m2...."+ str(cls) + "--- " + str(A.count)  + " --- using cls -- "+ str(cls.count))
        cls.m3()
        # cls.m1(A(), "argsdfsdf")
        # self = A()
        # self.m1("Asdasd")

    @classmethod
    def m3(cls):
        print(" class level method... m3 :: ")
        print(cls.m4(5))

    @staticmethod
    def m4(max):
        print("This is static... independant of class and object....")
        # a = A() to call instance methods....
        # a.m1()
        # to call class level
        # A.m2()
        return "-".join(str(item) for item in range(1,max))

if __name__ == "__main__":
    a = A()# object creation/instantiation
    # a --> reference variable of Object of type A
    a.m1("dusra argument ")
    print(A)
    A.m2()
    print(A.m4(10))
