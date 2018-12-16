
class A():

    def __init__(self):
        # super().__init__()
        self.nameOfObjectA = "This is variable of A"

        print("construcotr of A")

    def m1(self):
        print("m1 of class A")


if __name__ == "__main__":
    a = A()
    print("this is main " + __name__)
