import mysql.connector


class Db:
    @staticmethod
    def get_connection():
        con = mysql.connector.connect(user='root', database='medi_client',host='127.0.0.1')
        return con