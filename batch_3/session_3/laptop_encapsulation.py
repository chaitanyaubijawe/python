
# Class in python.....(Encapsulation)
class Laptop:

    # class level variable
    typeOfLaptop=""

    def __init__(self, name):
        print("This is constructor.... called automatically.... on instantiation(object creation )...")
        print("it is exactly similar to method.. except the fact that is gets called automatically.")
        # instance variable.
        print("printing info of self :: " + str(self))
        self.name = name

    def getName(self):
        return self.name

    @classmethod
    def getTypeOfLaptop(cls):
        return cls.typeOfLaptop

    def getTypeOfLaptopWithoutDecorator(cls):
        return cls.typeOfLaptop

    @staticmethod
    def getDateTime():
        # utility purpose..
        # return "current Time..."
        from datetime import datetime
        return datetime.now()


if __name__ == "__main__":
    Laptop.typeOfLaptop = "DELL"
    # object / instance of a class laptop
    notebook = Laptop(name = "Notebook Pro")

    print("Name of instance variable is  :: " + notebook.name)
    print("typeOfLaptop Class level variable is :: " + Laptop.typeOfLaptop)
    macbook = Laptop(name = "Macbook Pro")

    print("Name of instance variable is  :: " + macbook.name)
    print("typeOfLaptop Class level variable is :: " + Laptop.typeOfLaptop)
    macbook.typeOfLaptop = "Apple"

    print("typeOfLaptop :: instance : " + macbook.typeOfLaptop)
    print("typeOfLaptop Class level variable is :: " + Laptop.typeOfLaptop)

    print("Calling getName " + macbook.getName())
    print("Calling getTypeOfLaptop " + Laptop.getTypeOfLaptop())

    # without decorator calling a class level method.... refer code row no: 26 and 27 def getTypeOfLaptopWithoutDecorator(cls):
    print("Calling getTypeOfLaptop " + Laptop.getTypeOfLaptopWithoutDecorator(Laptop))

    print("Static method calling : " + str(Laptop.getDateTime()))

    # write calculator program in class fashion....
