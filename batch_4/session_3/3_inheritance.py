class A:

    def __init__(self):
        print("A here....")

    def m1(self):
        print("M1 of A")

class B(A):
    def __init__(self):
        # super() to call parent class methods and variables....
        super().__init__()
        print("B here....")

    def m2(self):
        print("M2 of B")


if __name__ == "__main__":

    b = B()

    b.m2()
    # a = A()
    b.m1()
