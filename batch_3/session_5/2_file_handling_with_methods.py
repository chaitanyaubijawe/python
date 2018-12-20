


# print(line_data)

def process_data(line_data, separator):
    for row in line_data:
        row_line_data = row.split(separator)
        # print(str(row) + str(row_line_data))

        print(row_line_data[0] +  row_line_data[1] + row_line_data[2] + row_line_data[3])
        sr_no = row_line_data[0]
        bagic_key = row_line_data[1]
        transaction_id = row_line_data[2]
        merchant_id = row_line_data[3]
        csc_transaction_no = row_line_data[4]

if __name__ == "__main__":
    file = open("a.csv",mode="r")
    content = file.read()
    line_data = content.splitlines()

    separator = ","
    process_data(line_data, separator)
    # separator = "|"
    # process_data(line_data, separator)
