def get_full_name():
    pass


class Person:
    ''' Object is the instance of class.
    Class is a blueprint of object......
    What is attributes?
    - Attributes/properties of a class means
        - variables
        - methods/functions
    Instantiation :
        creating instance of object..'''

    def __init__(self, name, last_name, age):
        ''' __init__ : is a function/method, which will be triggered automaticlly
        at the time of object creation/Instantiation.

        Significance: You can initialize any properties of a class at the time of Instantiation
        These variables are instance variables. '''
        self.name = name
        self.last_name = last_name
        self.age = age
        self.full_name = self.name + " " + self.last_name

    def get_full_name(self):
        '''This method is instance method.....'''
        return self.name + " __ " + self.last_name


''' person: reference variable holding reference of object Person. '''
''' Adding properties(instance variables...) to object.'''

mitesh = Person("Mitesh", "Joshi", 20)
# mitesh.name = "Mitesh..."
# mitesh.last_name = "Joshi....."

chaitanya = Person("Chaitanya", "Bijawe", 30)
# chaitanya.name = "Chaitanya ..."
# chaitanya.last_name = "Bijawe....."


print("Name of Person is ", mitesh.name, mitesh.last_name, mitesh.age, mitesh.full_name, mitesh)
print("Name of Person is ", chaitanya.name, chaitanya.last_name, chaitanya.age, chaitanya.full_name, chaitanya)

## instance methods/functions
name_mitesh = mitesh.get_full_name()
print(" Instance Methods get_full_name : ", name_mitesh)
print(" Instance Methods get_full_name : ", chaitanya.get_full_name())


class Employee1:

    def set_property(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def set_property_salary(self, sal):
        self.sal = sal


emp = Employee1()
emp.set_property("Mitesh", "Joshi", 29)
emp.set_property_salary(1000000)
print(emp.name, emp.sal)
