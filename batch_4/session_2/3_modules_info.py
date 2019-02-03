


import sys
sys.path.append("/Users/chaitanya/CB/python_training/python-sessions/batch_4/")

from session_2.module_1 import one


if __name__ == "__main__":

    one.m1()
    print(__name__)
    print(__package__)
    print(dir(dict))
    print(dir(list))
    print(dir(one))
    print(dir(__builtins__))
