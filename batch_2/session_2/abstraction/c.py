from abc import ABC, abstractmethod

class C(ABC):

    @abstractmethod
    def m3(self):
        pass

    def m4(self):
        print("own implementation")
