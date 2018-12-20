#1. write simple script without method to read content of file....
#2. write simple script with method to read content of file....
#3. write simple script with classes n methods read content of file....



# file = open("/Users/chaitanya/CB/python_training/python-sessions/batch_3/session_4/a.csv")

file = open("a.csv",mode="r")

print(str(file) + str(type))
content = file.read()

print(type(content))

### this will
# for line_data in content.split(","):
#     print(line_data)
# print(content.split(","))
# print(content.splitlines())

#line_data = content.split(",")
line_data = content.splitlines()


# print(line_data)

separator = ","
for row in line_data:
    row_line_data = row.split(separator)
    # print(str(row) + str(row_line_data))

    print(row_line_data[0] +  row_line_data[1] + row_line_data[2] + row_line_data[3])
    sr_no = row_line_data[0]
    bagic_key = row_line_data[1]
    transaction_id = row_line_data[2]
    merchant_id = row_line_data[3]
    csc_transaction_no = row_line_data[4]
