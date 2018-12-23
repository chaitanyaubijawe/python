from c import C
class D(C):

    def m3(self):
        print("implementation goes here....")


    def m5(self):
        print("free to write own methods as well...")


if __name__ == "__main__":

    d = D()
    d.m3()
    d.m4()
    d.m5()
