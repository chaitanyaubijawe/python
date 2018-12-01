from address import Address
from employee import Employee
import mysql.connector
from mysql.connector import MySQLConnection

class Utility:

    def start_processing(self, fileName):

        # STEP-1: Read csv file.
        # STEP-2: Map each row from csv to Python Objects. for e.g. Employee , Address and so on..
        # STEP-3: Collect each object into list.
        # STEP-4: return list
        employees = self.map("../names.csv")
        # print(file_content_list)
        # STEP-5: Iterate on list of employees
        # STEP-6: On each employee object generate insert query.
        # STEP-7: Get DB connection
        # STEP-8: Using DB connection execute insert query.

        self.insert_data(employees)

    def map(self, file_name):
        myfile = open(file_name)
        row_content = myfile.read()
        # print(row_content)
        rows = row_content.splitlines()
        # print(rows)

        employees_list = []

        ## Mapp object from csv to python objects.
        for row in rows:
            data = row.split(",")
            employee = Employee(data[0], data[1], data[2], data[3], Address.get_instance(data[4]),
                                Address.get_instance(data[5]))

            employees_list.append(employee)

        return employees_list

    def insert_data(self, employees):

        for emp in employees:
            query = self.generate_query(emp)
            con = self.get_connection()
            cursor = con.cursor()
            print("Executing employee query : ", query)
            cursor.execute(query)
            emp_id = cursor.lastrowid

            emp.set_emp_id(emp_id)

            emp.addr_1.set_emp_id(emp_id)
            emp.addr_2.set_emp_id(emp_id)

            addr_1_query = self.generate_query_addr(emp.addr_1)
            addr_2_query = self.generate_query_addr(emp.addr_2)
            print("Executing address-1  query : ", addr_1_query)
            cursor.execute(addr_1_query)
            # get generated address id and set it to address object present inside employee....
            addr_id_1 = cursor.lastrowid
            ##
            emp.addr_1.set_addr_id(addr_id_1)

            print("Executing address-1  query : ", addr_2_query)
            cursor.execute(addr_2_query)
            addr_id_2 = cursor.lastrowid
            ##
            emp.addr_2.set_addr_id(addr_id_2)

            con.commit()
            cursor.close()
            con.close()

    def generate_query_addr(self, addr):
        # print(file_content_list)
        Query = "INSERT INTO address (addr_line_1,addr_line_2,city,pincode,country,emp_id) VALUES ( '"
        Query += addr.address_line_1 + "','" + addr.address_line_2 + "','" + addr.city + "','" + str(
            addr.zip_code) + "','" + addr.country + "','" + str(addr.emp_id) + "')"
        return Query

    def generate_query(self, emp):
        Query = "INSERT INTO employee (name,last_name,age) VALUES ('"
        Query += emp.f_name + "','" + emp.l_name + "','" + emp.age + "')"
        return Query

    def get_connection(self):
        mysql.connector.connect()
        #cnx = mysql.connector.connect(user='joe', database='test')
        cnx = MySQLConnection(user='root', database='medi_client', port = 3306, host = "localhost")
        return cnx


if __name__ == '__main__':
    utility = Utility()
    utility.start_processing()