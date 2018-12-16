# abstract class...
# class A:
#     def m(self):
#         pass

########################

# from abc import ABC, abstractmethod
# you cannot instantiat abract class with abstract method in it.
# 1. create subclass n provide implementation of abstract method
# 2. Remove abstractmethod from abstract class in ordsr to instantiate
# class A(ABC):
#
#     @abstractmethod
#     def m(self):
#         pass


# from abc import ABC, abstractmethod
#
# class A(ABC):
#
#     def m(self):
#         pass
#     #
    # def m2(self):
    #     print("implementation")



from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m(self):
        pass
