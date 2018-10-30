from abc import ABC, abstractmethod

from address import Address
from employee import Employee


class BaseMapper(ABC):

    @staticmethod
    @abstractmethod
    def map(file_name):
        ...

class CSVMapper(BaseMapper):

    @staticmethod
    def map(file_name):
        myfile = open(file_name)
        row_content = myfile.read()
        #print(row_content)
        rows = row_content.splitlines()
        #print(rows)

        employees_list = []

        ## Mapp object from csv to python objects.
        for row in rows:
            data = row.split(",")
            # addr_1_pipe_separated  = data[4].split("|")
            # addr_1 = Address(addr_1_pipe_separated[0], addr_1_pipe_separated[1], addr_1_pipe_separated[2], addr_1_pipe_separated[3], addr_1_pipe_separated[4])
            #
            # address_2_pipe_separated = data[5].split("|")
            # address_2 = Address(address_2[0], address_2[1], address_2[2], address_2[3], address_2[4])

            employee = Employee(data[0], data[1], data[2], data[3], Address.get_instance(data[4]),
                                Address.get_instance(data[5]))

            employees_list.append(employee)

        return employees_list

class XLSMapper(BaseMapper):

    @staticmethod
    def map(file_name):
        ## treat your way to deal with xls files.
        myfile = open(file_name)
        row_content = myfile.read()
        #print(row_content)
        rows = row_content.splitlines()
        #print(rows)

        employees_list = []

        ## Mapp object from csv to python objects.
        for row in rows:
            data = row.split(",")
            # addr_1_pipe_separated  = data[4].split("|")
            # addr_1 = Address(addr_1_pipe_separated[0], addr_1_pipe_separated[1], addr_1_pipe_separated[2], addr_1_pipe_separated[3], addr_1_pipe_separated[4])
            #
            # address_2_pipe_separated = data[5].split("|")
            # address_2 = Address(address_2[0], address_2[1], address_2[2], address_2[3], address_2[4])

            employee = Employee(data[0], data[1], data[2], data[3], Address.get_instance(data[4]),
                                Address.get_instance(data[5]))

            employees_list.append(employee)

        return employees_list


class JSONMapper(BaseMapper):

    @staticmethod
    def map(file_name):
        myfile = open(file_name)
        row_content = myfile.read()
        #print(row_content)
        rows = row_content.splitlines()
        #print(rows)

        employees_list = []

        ## Mapp object from csv to python objects.
        for row in rows:
            data = row.split(",")
            # addr_1_pipe_separated  = data[4].split("|")
            # addr_1 = Address(addr_1_pipe_separated[0], addr_1_pipe_separated[1], addr_1_pipe_separated[2], addr_1_pipe_separated[3], addr_1_pipe_separated[4])
            #
            # address_2_pipe_separated = data[5].split("|")
            # address_2 = Address(address_2[0], address_2[1], address_2[2], address_2[3], address_2[4])

            employee = Employee(data[0], data[1], data[2], data[3], Address.get_instance(data[4]),
                                Address.get_instance(data[5]))

            employees_list.append(employee)

        return employees_list