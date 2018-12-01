class A:
    cv = 0

    def __init__(self, iv):
        self.iv = iv

    def getIv(self):
        return self.iv

    @classmethod
    def getCv(cls):
        return cls.cv

    def getCvSelf(self):
        return self.cv

    def setCV(self, cv):
        self.cv = cv

    # another way of writing class method. it is highly dependent on how you call this method
    # see line no 62:  A.getCvMiteshClassMethod(A)
    def getCvMiteshClassMethod(cls):
        return cls.cv


if __name__ == '__main__':
    a = A(5)
    print(a.getIv())#5
    print(a.iv)#5

    print("A.cv :: ",A.cv)#0

    print(a.__dict__) #namespace

    A.cv = 5
    print("A.cv :: ",A.cv)#5
    print("a.cv :: ",a.cv)#5


    a2 = A(15)
    print("a2.cv :: ",a2.cv)#5
    A.cv = 10
    print("a2.cv :: ",a2.cv)#10
    print("a.cv :: ",a.cv)#10
    a.cv = 50
    print("a.cv :: ",a.cv)#50# instance variable....
    print("a.getCv :: ",a.getCv())#10# instance variable....
    print("a.getCvSelf :: ",a.getCvSelf())#50# instance variable....
    print("a2.cv :: ",a2.cv)#10
    print("a2.getcv() :: ",a2.getCv())#10

    print("a2.getCvSelf() :: ",a2.getCvSelf()) #none undefined
    A.cv = 100
    print("a2.getCvSelf() :: ",a2.getCvSelf()) #100 undefined

    a2.setCV(500)

    print("a2.getCvSelf() :: ",a2.getCvSelf()) #500 undefined

    print("a2.getCvSelf() :: ",a2.getCv()) #100 undefined

    print(A.getCvMiteshClassMethod(A))







