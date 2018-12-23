import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', database='bajaj_insurance', port=3306, host="localhost")

cursor = cnx.cursor()

query = "select * from insurance_transaction where transaction_id like '%t%'"


cursor.execute(query)

for (c1, c2, c3) in cursor:
    print(str(c1)+ str(c2) + str(c3))

cursor.close()
cnx.close()