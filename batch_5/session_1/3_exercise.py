d = [{"tag":"Official", "number" :"8983237271"},{"tag":"Personell", "number" :"1234567890"} ]

# dd = d[0]
# dd = d[1] # {"tag":"Official", "number" :"8983237271"}
for dd in d:
    print(dd["tag"]) # official
    print(dd["number"]) # 8983237271

print("-------------------------------")
'''
# World:
IND -
    - MAH
        - Pune
        - Mumbai
        - NAGPUR
    - MP
        - Jabalpur
        - Indoor
    - UP
        - Lucknau
        - sdfsdfsd

USA -
    - CT
        - Danbury
        - City_2
    - ABC
        - City_3
        - City_4
'''


world ={
"IND" :
    {
    "MAH":["C1", "C2"],
    "MP":["C3", "C4"],
    "UP":["C5", "C6"]
    },
"USA" :
    {
    "ST1":["C1", "C2"],
    "ST2":["C3", "C4"],
    "ST3":["C5", "C6"]
    }
}

for countryName in world:
    print(countryName)
    stateMap = world[countryName]
    # print(stateMap)
    for stateName in stateMap:
        print("\t - " + stateName)
        cities = stateMap[stateName]
        for cityName in cities:
            print("\t \t - " + str(cityName))




print("-------------------------------")


bankAccounts = [{"name":"Chaitanya Bijawe", "accntNum":"123456789"}, {"name":"Chaitanya Bijawe", "accntNum":"123456789"}, {"name":"Chaitanya Bijawe", "accntNum":"123456789"}, {"name":"Chaitanya Bijawe", "accntNum":"123456789"}]


d = {"k1":"v1", "k2":"v2"}

var = ""
for key in d:
    var = var + key + " : " + d[key] + ","

# print(var[ :len(var)])

# Datatype set = {}



# Write a logic to find/count duplicate values from list.
