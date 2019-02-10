class A:
    def m1(self):
        print("Inside A m1.")


class B(A):
    def m2(self):
        print("Inside B m2.")

    def m_common(self):
        print("Inside m_common OF class B")


class C(A):
    def m3(self):
        print("Inside C m3.")

    def m_common(self):
        print("Inside m_common OF class C")


class D(C,B):

    def shuffleInheritance(self, c1, c2):
        self.__class__.__bases__ = (c1, c2,)

    def m4(self):
        print("Inside D m4.")


if __name__ == "__main__":

    # b = B()
    # c = C()
    # b.m1()
    # c.m1()

    d = D()
    d.m2()
    d.m3()
    d.m4()
    d.m_common()
    d.shuffleInheritance(B,C)
    d.m_common()

    D().m2()
