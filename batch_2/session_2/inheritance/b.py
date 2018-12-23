from a import A
from c import C

class B(A, C):

    def __init__(self):
        #super().__init__()
        self.var_b = "variable B of class B"

    def m2(self):
        print("method m2 of class B")
        # self.m1()
        # super().m1()



if __name__ == "__main__":

    b = B()
    b.m2()
    b.m1()

    print(b.var_b)
    #print(b.var_a)
