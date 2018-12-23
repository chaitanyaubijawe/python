class C:

    def __init__(self):
        self.var_c = "this is var from class C"
        print("inside constructor of C....")

    def m1(self):
        print("method of class C")
        self.var_c = "this is var from class C"
