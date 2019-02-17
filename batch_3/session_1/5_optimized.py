import sys
fileObj = open(sys.argv[0], "r")

# inputData = "1 2 3 4 5 6 6 7 7 8 8 5 76 8 32"
# args = ["1-5", "6-10"]

args = sys.argv[2:]

buffersize = 20
output = {}
inputFile = open("input.txt", "r")
inputData = inputFile.read(buffersize)

while len(inputData):
    for item in args:
        if item not in output.keys():
            output[item] = 0
        data = item.split("-")
        num_1 = int(data[0])
        num_2 = int(data[1])
        # r = range(int(num_1), int(num_2)+1)


        for num in inputData.split(" "):
            if num.isnumeric() and num_1 <= int(num) <= num_2:
                counter = output[item]
                output[item] = counter + 1
    inputData = inputFile.read(buffersize)



for item in output:
    print(item + " count is :: " + str(output[item]))