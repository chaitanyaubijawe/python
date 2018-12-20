class Transaction:

    def __init__(self, row_line_data):
        self.sr_no = row_line_data[0]
        self.bagic_key = row_line_data[1]
        self.transaction_id = row_line_data[2]
        self.merchant_id = row_line_data[3]
        self.csc_transaction_no = row_line_data[4]
