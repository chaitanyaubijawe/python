class Person:
    pass


class Employee:


    increment = 1.10
    num_of_employess = 0

    def get_fName(self):
        return self.f_name

    def __init__(self, name, l_name):
        self.name = name
        self.l_name = l_name
        self.f_name = name + " " + l_name
        self.email = name + "." + l_name + "@sears.com"
        self.increment = 1.20

    def set_increment(self, increment):
        '''Intance method takes self implicitly as a first argument.
         Python interpreter sends reference variable holding object of a class to these methods in self'''
        self.increment = increment

    @classmethod
    def set_increment_class_method(cls, increment):
        ''' @classmethod is a decorator.
        It is logically converting a method  to pass cls as a first argument.'''
        cls.increment = increment

    @classmethod
    def m2_another_class_method(cls):
        print("Called using Class Employee...")
        cls.increment = 2.0

    @classmethod
    def get_instance(cls, name, l_name):
        cls.num_of_employess += 1
        #return Employee(name, l_name)
        return cls(name, l_name)

    @classmethod
    def get_instance_csv(cls, csv):
        name, l_name = csv.split(",")
        return cls(name, l_name)

    @staticmethod
    def utility_is_admin(arg):
        return arg == "ADMIN"


if __name__ == '__main__':
    '''Instantiating person class.
        Class is :: blueprint of an object..
        Object is instance of  a class.
        
        Attributes: 
            - These are properties of a class. Can be variable and function.
        Instance Variable and Method:
            - Variables or methods which can be access by using self.
    '''
    person = Person()
    person.name = "Nimesh"
    person.l_name = "Shroti"
    print(person.name)
    print(person.l_name)
    # nimesh,shroti
    # chaitanya,bijawe

    csv = "chaitanya,bijawe"

    l_employees = "nimesh,shroti".split(",")

    nimesh = Employee(l_employees[0], l_employees[1])
    chaitanya = Employee.get_instance_csv(csv)
    #admin = Employee.get_instance_csv("ADMIN,ADMIN")

    print("Namespace using reference variable:: ", nimesh.__dict__)
    print("Namespace using Class :: ", Employee.__dict__)

    print("Name of nimesh :: ", nimesh.name, " Email of nimesh:: ", nimesh.email)

    print("Get_fname:: ", nimesh.get_fName())

    print(Employee.get_fName(nimesh))

    print(Employee.get_fName(chaitanya))

    print(nimesh.increment, Employee.increment)
    Employee.increment = 1.5
    print(chaitanya.increment, Employee.increment)

    nimesh.set_increment(1.7)
    Employee.set_increment_class_method(1.8)

    Employee.m2_another_class_method()# passing class.

    print("Nimesh should get 1.7 :: ", nimesh.increment, Employee.increment)
    print(chaitanya.increment, Employee.increment, Employee.num_of_employess)



    print("Calling static method nimesh", Employee.utility_is_admin("Nimesh"))

    print("Calling static method ", chaitanya.utility_is_admin("ADMIN"))
    print("Calling static method nimesh", chaitanya.utility_is_admin("Nimesh"))


import datetime
