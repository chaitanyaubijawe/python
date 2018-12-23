
from session_6.sql_with_class_4.query_helper import QueryHelper
from session_6.sql_with_class_4.insurance import Insurance
from session_6.sql_with_class_4.connection import Connection

class InsuranceTransactionRepository:

    def __init__(self):
        self.queryGenerator = QueryHelper()
        self.connectionObj = Connection()


    def execute_select(self):
        # query = self.queryGenerator.get_select_query({"transaction_id": "abhishekTomars"})
        query = self.queryGenerator.get_select_query()
        con = None
        cursor = None
        insuranceList = []
        try:

            con = self.connectionObj.get_connection()
            cursor = con.cursor()
            cursor.execute(query)
            # Mapping DB to Python Objects.....
            for (c1, c2, c3) in cursor:
                #print(str(c1)+ str(c2) + str(c3))
                insuranceList.append(Insurance(c1,c2,c3))
        except Exception as e:
            print("Error :: " + str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

        return insuranceList


    def execute_insert(self, transaction):
        query = self.queryGenerator.get_insert_query(transaction)
        con = None
        cursor = None
        result = None
        try:

            con = self.connectionObj.get_connection()
            cursor = con.cursor()
            cursor.execute(query)

            result = cursor.rowcount

        except Exception as e:
            print("Error :: " + str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.commit()
                con.close()

        return result


if __name__ == "__main__":

    repo = InsuranceTransactionRepository()
    insuranceList = repo.execute_select()

    for insurance in insuranceList:

        print(insurance.id)