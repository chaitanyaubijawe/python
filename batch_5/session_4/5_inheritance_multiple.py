class A:

    def __init__(self):
        print("Parent A class constructor....")
        self.a = 5

    def m1(self):
        print("inside A parent m1")


class B():

    def __init__(self):
        print("Inside class B constructor")
        self.b = 10

    def m1(self):
        print("Inside class B m1")

class C(B,A):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)


    def m3(self):
        print("Inside class C m3" + str(self.__class__.__bases__ ) + " --- type :: " + str(type(self.__class__.__bases__ )))

    def shuffleInheritance(self, c1, c2):
        self.__class__.__bases__ = (c1, c2,)

if __name__ == "__main__":

    obj = C()
    print(obj.b)
    print(obj.a)
    # obj.m2()
    obj.m1()# m1 of B should get called...
    obj.m3()
    obj.shuffleInheritance(A,B)
    obj.m1()# m1 of A should get called...
