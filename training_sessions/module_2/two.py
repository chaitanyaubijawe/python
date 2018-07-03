#from module_1.one import *
import module_1.one

def hello_module_2():
    print("Hello from  module_2.two.py ")
    module_1.one.hello()
    module_1.one.hi()
def hi_2():
    print("hdsdi_2")
#hello_module_2()
if __name__ == "__main__":
    hello_module_2()
    import sys
    print(sys.path)
    print(dir(sys))
    import builtins
    print(dir(builtins))
    #print(__path__)
