from abc import ABC, abstractmethod


class A(ABC):
    @classmethod
    @abstractmethod
    def m1(nimesh):
        print("Hi there")

    @staticmethod
    @abstractmethod
    def m2(self):
        ...



class B(A):

    def m1(self):
        print("hi there", self)

class C(B):

    @staticmethod
    def m2(self):
        #self.a = 1
        print("hi there", self)


if __name__ == '__main__':
    b = C()
    b.m2("asdasd")