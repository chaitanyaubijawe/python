

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


def writeData(fileName, lines=[]):
    sg_data_file = open(fileName, "a")

    for line in lines:
        sg_data_file.write(line)

    sg_data_file.close()


def readFile(fileName):
    sg_data_file = open(fileName, "r")
    data = sg_data_file.read()
    print(data)
    sg_data_file.close()


lines = ["4,CodesNBugs,Education,India,12345","5,CodesNBugs,Education,India,12345" "6,CodesNBugs,Education,India,12345"]
fileName = "data.csv"

writeData(fileName, lines)
readFile(fileName)