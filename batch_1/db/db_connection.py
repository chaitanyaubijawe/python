import mysql.connector
from mysql.connector import MySQLConnection


class DBConnection:


    def get_connection(self):
        mysql.connector.connect()
        #cnx = mysql.connector.connect(user='joe', database='test')
        cnx = MySQLConnection(user='root', database='medi_client', port = 3306, host = "localhost")
        return cnx