class A:
    def __init__(self, var_1):
        self.var_1 = var_1
        print("Constructor of A", var_1)

    def m1(self):
        print("inside m1 of A")

    @classmethod
    def m3(cls):
        print("this is a class method")

if __name__ == '__main__':
    A().m1()
    A.m3()
