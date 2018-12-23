def performOperation(var_list, operationToBePerform):
    result = 0
    if operationToBePerform == "add":
        for elem in var_list:
            result += elem
        return result

inputList = [4, "+", 5]

var_list = []
operation = None
for elem in inputList:
    if str(elem).isdigit():
        var_list.append(elem)
        if len(var_list) == 2:
            result = performOperation(var_list, var_list)
            print(result)
    elif str(elem) == "+":
        operation = "add"
