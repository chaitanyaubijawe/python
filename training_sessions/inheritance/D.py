from A import A
from C import C
from B import B

class D(C,A):

    def shuffle(self, p1,p2):
        #self.__dict__.__class__(p1,p2) this does not work
        self.__class__.__bases__ = (p1, p2,)

    def md(self):
        print("Inside md of D class")