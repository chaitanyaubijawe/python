from address import Address


class Employee:
    def __init__(self,f_name, l_name,roll_num, age, addr_1,addr_2):
        self.f_name = f_name
        self.l_name = l_name
        self.roll_num = roll_num
        self.age = age

        #address_1 = addr_1.split("|")
        #address_2 = addr_2.split("|")

        self.addr_1 = addr_1
        self.addr_2 = addr_2

    def set_emp_id(self, id):
        self.emp_id = id

