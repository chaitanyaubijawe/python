from session_6.sql_with_class_4.insurance_transaction_repository import  InsuranceTransactionRepository
from session_6.sql_with_class_4.file_handling_with_class import TransactionDataProcessor

class Utility:

    def do_work(self):

        repo = InsuranceTransactionRepository()
        tp = TransactionDataProcessor()
        transactionsData = tp.process_data("a.csv", ",")


        for transaction in transactionsData:
            result = repo.execute_insert(transaction)

            print("Inserted record count :: " + str(result))

        insuranceList = repo.execute_select()

        for insurance in insuranceList:

            print(str(insurance.id) + "--- " + str(insurance.transaction_id)+ "--- " + str(insurance.csc_transaction_id))



if __name__ == "__main__":

    Utility().do_work()

