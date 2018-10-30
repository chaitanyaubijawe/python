class Address:
    def __init__(self, address_line_1, address_line_2, city, zip_code, country):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.zip_code = zip_code
        self.country = country

    def set_emp_id(self, id):
        self.emp_id = id

    def set_addr_id(self, id):
        self.addr_id = id

    @classmethod
    def get_instance(cls, addr_1_pipe_separated):
        addr_1_array = addr_1_pipe_separated.split("|")

        return cls(addr_1_array[0], addr_1_array[1], addr_1_array[2], addr_1_array[3],
                     addr_1_array[4])
