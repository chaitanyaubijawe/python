
class A:


    def m1(arg):
        print("hi there1", arg)
        return arg


    def m2(self, b = m1("Sefwfwfe")):
        print("hi there2 :: ", b)



    # def m1(self):
    #     print("Inside m1 of A")
    #     self.m3()
    #     print("Accessing B property :: ", self.bprop)


# class B(A):
#
#     def __init__(self):
#         self.bprop = "B ki property"
#
#     def m2(self):
#         print("Inside m2 of B")
#         super().m1()  ## 1
#         self.bprop_2 = "second property"
#         self.m1()  ## 2
#
#     def m3(self):
#         print("Inside m3 of B")


if __name__ == '__main__':
    b = A()
    #b.m2()
    b.m2(b=A.m1)
