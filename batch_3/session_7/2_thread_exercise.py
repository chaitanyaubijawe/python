import threading

from session_6.sql_with_class_4.file_handling_with_class import TransactionDataProcessor
from session_6.sql_with_class_4.insurance_transaction_repository import InsuranceTransactionRepository

def m():

    repo = InsuranceTransactionRepository()
    tp = TransactionDataProcessor()
    transactionsData = tp.process_data("/Users/chaitanya/CB/python_training/python-sessions/batch_3/session_6/sql_with_class_4/a.csv", ",")


    for transaction in transactionsData:
        result = repo.execute_insert(transaction)
        print("Inserted record count :: " + str(result))
        # print(transaction.__dict__)


t1 = threading.Thread(target=m, args=(), name="firstThread")
t2 = threading.Thread(target=m, args=(), name="SecondThread")


t1.start()
t2.start()

t2.join()
t1.join()

# TODO:  Lock: thread.acquire()
## make sure central object to be locked while working with thread..