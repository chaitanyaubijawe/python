from a import A

class B(A):

    def __init__(self):
        super().__init__()
        self.nameOfObjectB = "This is variable of B"

    def m2(self):
        print("m2 of class B")


if __name__ == "__main__":
    b = B()

    b.m2()
    print(b.nameOfObjectA)
    print(b.nameOfObjectB)
    # calling inherrited method of parent class
    b.m1()
    # traditional way of calling another class method...
    # a = A()
    # a.m1()

    print("this is main " + __name__ )
