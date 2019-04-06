class A:

    def __init__(self):
        print("Parent class constructor....")
        self.a = 5

    def m1(self):
        print("inside parent m1")


class B(A):

    def __init__(self):
        super().__init__()
        print("Inside class B constructor")
        self.b = 10

    def m2(self):
        print("Inside class B m2")

class C(B):
    def m3(self):
        print("Inside class C m3")

if __name__ == "__main__":

    obj = C()
    print(obj.b)
    print(obj.a)
    obj.m2()
    obj.m1()
    obj.m3()
