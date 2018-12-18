class A():

    def __init__(self):
        print("Parent constructor...")

class B(A):

    def __init__(self):

        print("child class constructor.....")
        super().__init__()


    def m(self):
        print("temp")

if __name__ == "__main__":
    b = B()
    b.m()
