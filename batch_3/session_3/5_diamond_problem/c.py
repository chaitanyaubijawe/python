from a import A
from b import B
# c is derrived from A and B
# C is having two parents A and B
# diamond problem....
# methods will be resolved in the order/sequence of Classes is derrived from....
class C(A,B):
    def __init__(self):
        # super().__init__()
        print("constructor of C")
        # pass


# class C(B,A):
#     def __init__(self):
#         # super().__init__()
#         print("constructor of C")
#         # pass
