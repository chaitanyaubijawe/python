class A:
    pass


class B(A):
    pass

class C:
    def __init__(self,a):
        print("hi there")

class D(C):

    def __init__(self, a):
        pass

    def m1(self):
        pass


if __name__ == '__main__':
    a = A()
    b = B()

    d =D(1)
    d.m1()

    print("A is subclass of B", issubclass(A,B))
    print("B is subclass of A", issubclass(B,A))
    print("a is instance of A ", isinstance(a,A))
    print("b is instance of B ", isinstance(b,B))
    print("a is instance of B ", isinstance(a,B))
    print("b is instance of A ", isinstance(b,A))