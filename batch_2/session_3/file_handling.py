class ServerInfo:
    def __init__(self, c1,c2,c3,c4):

        self.id = c1
        self.server_ip = c2
        self.ram = c3
        self.hardDisk = c4

def read_csv(fileName, sepator):

    try:

        fileObj = open(fileName, mode="r")
        print(type(fileObj))
        content = fileObj.read()

        line_data = content.splitlines()
        servers = []
        for line in line_data:
            row_data = line.split(sepator)
            #print(str(row_data[0]) + " ||| " + str(row_data[1]))
            servers.append(ServerInfo(row_data[0],row_data[1],row_data[2],row_data[3]))

        return servers


    except Exception as e:

        print("error while reading file....")
        return

def write_csv(fileName, sepator, mode="a"):

    try:

        fileObj = open(fileName, mode=mode)

        for i in range(10):
            line = ""
            for col in range(5):

                line += "value_" + str(col) + sepator

            line += "\n"

            fileObj.write(line)


        fileObj.close()

    except Exception as e:

        print("error while reading file....")
        return



def write_csv_data(fileName, sepator, data=[], mode="a"):

    try:

        fileObj = open(fileName, mode=mode)

        for  server in data:
            line = ""
            line += str(server.id) + sepator + str(server.server_ip) + sepator + str(server.ram) + sepator + str(server.hardDisk)

            line += "\n"

            fileObj.write(line)


        fileObj.close()

    except Exception as e:

        print("error while reading file....")
        return

if __name__ == "__main__":

    servers = read_csv("a.csv", ",")

    for server in servers:

        print(str(server.id) +  "---- " + server.ram)



    write_csv("w.csv", ",", mode="w")
    write_csv_data("d.csv", ",", data=servers, mode="w")
