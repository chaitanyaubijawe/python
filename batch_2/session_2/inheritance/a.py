class A:

    def __init__(self):
        self.var_a = "this is var from class A"
        print("inside constructor of A....")

    def m1(self):
        print("method of class A")
        self.var_a = "this is var from class A"
