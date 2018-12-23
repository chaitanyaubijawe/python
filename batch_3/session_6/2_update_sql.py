import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', database='bajaj_insurance', port=3306, host="localhost")

cursor = cnx.cursor()

# query = "UPDATE insurance_transaction set transaction_id = 'abhishek tomar' where idinsurance_transaction=1"
query = "UPDATE insurance_transaction set transaction_id = 'abhishekT'"


cursor.execute(query)

# this will give you results count which are affected....
cursor.rowcount


print("result : " + str(cursor.rowcount))


cursor.close()
cnx.commit()
cnx.close()