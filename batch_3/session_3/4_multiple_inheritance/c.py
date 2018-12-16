from a import A
class C(A):
    def __init__(self):
        super().__init__()
        print("constructor of C")
