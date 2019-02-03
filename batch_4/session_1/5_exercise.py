d = {
    "IND" : {
            "MAH":["PUNE" , "MUMBAI", "NAG"],
            "MP":["JBL" , "INDR"]
            },
    "US" : {
            "ST1":["C1" , "C2"],
            "ST2":["C3" , "C4"]
            }
}


for countryName in d:
    stateMap = d[countryName]
    for stateName in stateMap:
        cities = stateMap[stateName]
        for city in cities:
            print("COuntry :: " + countryName + " -- State name :: " + stateName + " -- City :: " + city)




print(d["IND"]["MAH"])

stateMap = d["IND"]
cities = stateMap["MAH"]

cities.append("KOLHAPUR")

cities.remove("MUMBAI")

# d["IND"]["MAH"]

print(d["IND"]["MAH"])
