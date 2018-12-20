import json

file = open("aa.json",mode="r")

content = file.read()
transactionData = json.loads(content)

# print(transactionData)


for transaction in transactionData:
    print(transaction["bagic_key"])


##TODO: ecommerce data into json....
