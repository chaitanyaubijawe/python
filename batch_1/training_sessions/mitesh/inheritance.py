#from A_inheritance import A
import A_inheritance


# B is subclass of A.
# B is A.
# A is parent

class B(A_inheritance.A):
    def __init__(self):
        super().__init__(2)
        print("Constructor of B")

    def m2(self):
         self.m1()
         # instance method
         # class method method
         super().m3()

if __name__ =='__main__':
    b = B()
    # b.m1()
    b.m2()
    b.var_1
