
import mysql.connector
from mysql.connector import Error

from batch_4.session_5.CompanyInfo import CompanyInfo


class DBConnection:


    def connect(self):
        """ Connect to MySQL database """
        conn = None
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='sg_analytics',
                                           user='root',
                                           port=3306
                                           )
            if conn.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)

        # finally:
        #     if conn is not None:
        #         conn.close()
        return conn

    def insert_company(self,comp):
        query = "INSERT INTO comapny_info(`comp_id`,`name`,`sector`,`country`,`revenue`)  VALUES('" + str(comp.compId) + "','" + str(comp.compName) + "', '" + str(comp.sectorName) + "','" + str(comp.country) + "','" + str(comp.revenue) + "')"
        cursor = None
        conn = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            print("Executing query :: " + query)
            cursor.execute(query)
            conn.commit()
        except Error as e:
            print('Error:', e)

        finally:
            if cursor is not None:

                cursor.close()
            if conn is not None:
                conn.close()

    def select_company(self):
        dataDb = []
        query = "select * from comapny_info where name like '%C%'"
        cursor = None
        conn = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            print("Executing query :: " + query)
            cursor.execute(query)
            resultSet = cursor.fetchall()
            for data in resultSet:
                comp = CompanyInfo(data[0], data[1], data[2], data[3], data[4])
                dataDb.append(comp)


        except Error as e:
            print('Error:', e)

        finally:
            if cursor is not None:

                cursor.close()
            if conn is not None:
                try:

                    conn.close()
                except Error as e:
                    print("Error: ",e )

        return dataDb


if __name__ ==  "__main__":

    DBConnection().connect()
