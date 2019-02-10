sg_data_file = open("data.csv", "r")
data = sg_data_file.read()

#print(type(data))
comp_list = data.splitlines()
#print(type(comp_list))
for company in comp_list:
    columns = company.split(",")
    print(str(columns[0]) + " // " + str(columns[1]) + " // " + str(columns[2]) + " // " + str(columns[3]))
    #print("------------")
sg_data_file.close()

print("After reading the file")

sg_data_file = open("data.csv", "a")
add_line = "4,CodesNBugs,Education,India,12345"
sg_data_file.write(add_line)
sg_data_file.close()


sg_data_file = open("data.csv", "r")
data = sg_data_file.read()
print(data)
sg_data_file.close()
