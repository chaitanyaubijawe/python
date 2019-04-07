

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def m1(self):
        pass

    def m3(self):
        print("This is complete method inside abstract class...")


class B(A):

    def m11(self):
        print("this is implementation inside child class...")

    def m2(self):
        print("this is implementation...")


class C(B):
    def m1(self):
        print("this is implementation inside child class C...")

if __name__ == "__main__":
    ''' inherit class from ABC'''
    ''' decalre method as @abstractmethod...'''
    ''' you cannot instantiate abstract class'''
    a = C()
    a.m1()
    a.m3()
