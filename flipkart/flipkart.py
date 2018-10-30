from flask import Flask, json, request, render_template
import logging
import mysql.connector
from mysql.connector import MySQLConnection


FORMAT = '%(asctime)-15s %(filename)-5s %(funcName)-5s %(message)s'
logging.basicConfig(format=FORMAT, level="DEBUG")

logger = logging.getLogger("scope.test")

logger.setLevel("DEBUG")


app = Flask(__name__)


@app.route('/product', methods=['POST'])
def add_product():
    result = None
    # read data from request.....
    product_data = request.get_json() # string::
    #data = {"name":"iphone 10", "price":50000, "description":"This is an awesome phone...", "color":"RED", "url":"https://images-na.ssl-images-amazon.com/images/I/71x3e0x%2BM2L._SL1382_.jpg" }

    # FORM: Insert query?
    query = generate_add_product_query(product_data)

    # create a db connection...
    con = get_connection()
    cursor = con.cursor()
    # Execute query....
    cursor.execute(query)
    product_id = cursor.lastrowid
    # web client: send product id along with other required data...
    product_data["id"] = product_id
    # this part is forming response....into json format...
    result = json.jsonify(product_data)

    con.commit()
    cursor.close()
    con.close()

    logger.debug("debug Printing result object....")
    return result, 200



@app.route('/')
def staticFileServing():
    return render_template('index.html')


def get_connection():
    mysql.connector.connect()
    cnx = MySQLConnection(user='root', database='flipkart', port = 3306, host = "localhost")
    return cnx


def generate_add_product_query(data={}):

    # INSERT into products(name, price,description, color, url) VALUES ('iphone',50000,'This is an awesome phone','RED' ,'url');
    # data = {"name":"iphone 10", "price":50000, "description":"This is an awesome phone...", "color":"RED", "url":"https://images-na.ssl-images-amazon.com/images/I/71x3e0x%2BM2L._SL1382_.jpg" }
    query = "INSERT into products("
    for key in data.keys():
        if key == 'id':
            continue
        else:
            query += key + ", "

    query = query[:-2]
    query += ") VALUES ('"

    for key in data.keys():
        query += str(data[key]) + "', '"

    query = query[:-3]
    query += ");"

    logger.debug("Executing query :: " + query)
    return query
#
# if __name__ == '__main__':
#     generate_add_product_query()

app.run(port=8080)