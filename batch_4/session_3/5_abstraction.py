from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        pass


    def m2(self):
        print("Can have non abstractmethod")


class B(A):

    def m1(self):
        print("OVERRIDE ::: Link your adhar here......")

    def m3(self):
        # calling supercalss method of abstract class..
        super().m2()

#Simple abstract class by conventions..
class C():
    # @abstractmethod
    def m1_c(self):
        pass

class D(C):
    def m1_c():
        print("implementation of method inside child class..")


if __name__ == "__main__":

    # A().m1()
    b  = B()
    b.m1()
    b.m2()
    b.m3()

    # c = C()
    # c.m1_c()
    # v = "String"
    # "String".count("S")
    # print("hello")
'''
Abstraction:
    - Abstraction means to have a incomplete(abstract) method Inside a class.
    - Abstract class cannot be instantiated.
    - Abstract class may or may not have abstract method.
    - Abstract class can have non abstract method as well.
'''
