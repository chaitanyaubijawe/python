from db.db_connection import DBConnection
from db.base_dao import BaseDao


class EmployeeDao(BaseDao):

    def __init__(self):
        super(EmployeeDao, self).__init__()
        #self.db = DBConnection()
        pass
        

    @staticmethod
    def generate_queries(file_content_list):
        # print(file_content_list)
        queries = []

        for emp in file_content_list:
            Query = "INSERT INTO employee (name,last_name,age) VALUES ('"
            Query += emp.f_name + "','" + emp.l_name + "','" + emp.age + "')"
            # print(emp)
            # print(Query)
            queries.append(Query)
        return queries

    @staticmethod
    def generate_query(emp):
        # print(file_content_list)
        Query = "INSERT INTO employee (name,last_name,age) VALUES ('"
        Query += emp.f_name + "','" + emp.l_name + "','" + emp.age + "')"
        return Query

    @staticmethod
    def generate_query_addr(addr):
        # print(file_content_list)
        Query = "INSERT INTO address (addr_line_1,addr_line_2,city,pincode,country,emp_id) VALUES ( '"
        Query += addr.address_line_1 + "','" + addr.address_line_2 + "','" + addr.city + "','" + str(addr.zip_code) + "','" + addr.country + "','" + str(addr.emp_id) + "')"
        return Query

    def insert_with_inheritance(self, employees):

        for emp in employees:
            query = EmployeeDao.generate_query(emp)
            ######
            # id = super().insert(query)
            id = self.insert(query)
            print("inserted emp is : ", id)


    def insert_data(self, employees):

        # queries = EmployeeDao.generate_queries(employees)
        # queries = EmployeeDao.generate_queries_user()
        # print(queries)

        for emp in employees:
            query = EmployeeDao.generate_query(emp)
            con = self.db.get_connection()
            cursor = con.cursor()
            cursor.execute(query)
            emp_id = cursor.lastrowid

            emp.set_emp_id(emp_id)

            emp.addr_1.set_emp_id(emp_id)
            emp.addr_2.set_emp_id(emp_id)

            addr_1_query = EmployeeDao.generate_query_addr(emp.addr_1)
            addr_2_query = EmployeeDao.generate_query_addr(emp.addr_2)
            cursor.execute(addr_1_query)
            # get generated address id and set it to address object present inside employee....
            addr_id_1 = cursor.lastrowid
            ##
            emp.addr_1.set_addr_id(addr_id_1)

            cursor.execute(addr_2_query)
            addr_id_2 = cursor.lastrowid
            ##
            emp.addr_2.set_addr_id(addr_id_2)



            con.commit()
            cursor.close()
            con.close()

    # @staticmethod
    # def generate_queries_user():
    #     return ["insert into user(id,name) values(1,'asfasdasds')", "insert into user(id,name) values(1,'asfasdasds')"]
