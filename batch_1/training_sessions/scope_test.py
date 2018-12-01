def parent_method(arg):
    def m1():
        print("Inside m1 :: ", arg)

    def m2():
        print("inside m2 :: ", arg)

    m1()
    m2()


# parent_method("this is argument...")


w_map = "this is global"


def parent_method_keyword(arg):
    def m0():
        # method local variable.....
        w_map = "Method local variable..."

    def m1():
        # nonlocal w_map
        w_map = "non local scope assigning inside method...."

    def m2():
        global w_map
        w_map = "global scope is assinged....."

    # w_map = "This is method variable"
    # print("before W_map :: ", w_map)
    # m0()
    # print("after assigning value in local method.... W_map :: ", w_map)
    # m1()
    # print("after assigning value with nonlocal keyword.... W_map :: ", w_map)
    global w_map
    m2()
    print("after assigning value with global keyword.... W_map :: ", w_map)


# print("Golbal W_map :: ", w_map)
parent_method_keyword("this is argument...")
# print("Global keyword.... W_map :: ", w_map)
##################################################


world_map = {}


def world_map_creator():
    # world_map = {}
    def create_country_map():
        world_map = {}
        world_map["IND"] = {}
        print("Inside create_country_map ")

    def create_state_map():
        global world_map
        world_map["US"] = {}
        print("global variable")

    create_country_map()
    print("After modifying into create_country_map", world_map)
    create_state_map()
    print("After modifying into create_state_map", world_map)


world_map_creator()
print("Global map :: ", world_map)

import logging

FORMAT = '%(asctime)-15s %(filename)-5s %(funcName)-5s %(message)s'
logging.basicConfig(format=FORMAT, level="DEBUG")
logger = logging.getLogger("scope.test")
logger2 = logging.getLogger("scope.test")
# logger.setLevel("DEBUG")
logger.setLevel("INFO")
print(id(logger))
print(id(logger2))
logger.warning("hello")
logger.error("hello")
logger.debug("debug message....")


def print_something():
    logger = logging.getLogger("scope.test")
    print(id(logger))
    logger.info("info message....")


print_something()

# 4334185720
# 4334185720
# 2018-07-22 12:58:19,976 hello
# 2018-07-22 12:58:19,976 hello
# 4334185720
