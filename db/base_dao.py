from db.db_connection import DBConnection


class BaseDao:

    def __init__(self):
        self.db = DBConnection()

    def insert(self, query):
        con = None
        cursor = None
        try:
            con = self.db.get_connection()
            cursor = con.cursor()
            cursor.execute(query)
            row_id = cursor.lastrowid
            return row_id
        except Exception as e:
            pass
        finally:
            cursor.close()
            con.close()

    def select(self, query):
        pass

    def update(self, query):
        pass

    def delete(self, query):
        pass
