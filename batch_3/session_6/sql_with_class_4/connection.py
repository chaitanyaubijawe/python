import mysql.connector
class Connection:

    def get_connection(self):
        cnx = mysql.connector.connect(user='root', database='bajaj_insurance', port=3306, host="localhost")
        return cnx

    # close connection
    # connection commit
    ## connection rollback...
