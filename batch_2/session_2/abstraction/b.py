from a import A
class B(A):
    # implementation..... of m1 from A.... overriding...
    def m1(self):

        print("M1 of B:::")

if __name__ == "__main__":

    b = B()

    b.m1()
