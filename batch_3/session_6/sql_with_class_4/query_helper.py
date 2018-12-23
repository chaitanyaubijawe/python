class QueryHelper:

    def get_select_query(self, where_clause={}):

        query = "SELECT * from insurance_transaction"
        if len(where_clause.keys()) > 0:

            query = "SELECT * from insurance_transaction WHERE "
            for column in where_clause:
                query += column + " = '" + str(where_clause[column]) + "'"

        return query

    def get_insert_query(self, data):
        query = "insert into insurance_transaction (transaction_id, csc_transaction_id) values('" + data.transaction_id + "' , '" + data.csc_transaction_no + "') "

        return query


class Insurance:

    def __init__(self, c1, c2, c3):
        self.id = c1
        self.transaction_id = c2
        self.csc_transaction_id = c3


if __name__ == "__main__":
    q = QueryHelper()
    # query = q.select_query({"transaction_id":3})
    query = q.get_select_query({"csc_transaction_id": "csc_transaction"})
    print(query)
