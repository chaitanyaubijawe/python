class A:

    def __init__(self):
        print("Parent A class constructor....")
        self.a = 5

    def m1(self):
        print("inside A parent m1")


class B(A):

    def __init__(self):
        super().__init__()
        print("Inside class B constructor")
        self.b = 10

    def m1(self):
        super().m1()
        print("Inside class B m1")

if __name__ == "__main__":

    obj = B()
    print(obj.b)
    print(obj.a)
    # obj.m2()
    obj.m1()# m1 of B should get called...
