class A:
    def __init__(self):
        self.id = 1
        pass

    def m1(self):
        self.id = 1
        self.id

    def m2(self):
        self.m1()


a1 = A()
a2 = A()
