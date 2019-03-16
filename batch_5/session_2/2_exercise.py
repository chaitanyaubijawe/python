
# [] = [CITY_1, CITY_2,CITY_3, CITY_4, CITY_5]

def generate_cities(stateName, arg_1=1, arg_2=5):
    l = []
    for i in range(arg_1,arg_2+1):
        rs = stateName + "_CITY_" + str(i)
        l.append(rs)
    print("#CITIES#DONE#")
    return l
# cities = generate_cities("MAH",1,5)
# print(cities)



def stateMap(*args):
    #{"MAH":[CITY_1, CITY_2,CITY_3, CITY_4, CITY_5]}
    d = {}
    # d["MP"] = generate_cities("MP",6,11)
    # d["UP"] = generate_cities("UP",12,16)
    for item in args:
        d[item] = generate_cities(item)
        # d["MP"] = generate_cities("UP",6,11)
        # d["UP"] = generate_cities("MP",12,16)
    print("#STATE#DONE#")
    return d


# stateData = stateMap()
#
# print(stateData)

def worldMap():
    # {"IND":{"MAH":[], "UP":[]}}
    wmap = {}
    wmap["IND"] = stateMap("MP","UP","MAH")
    wmap["US"] = stateMap("CT","ABC")
    return wmap;


world  = worldMap()

# print(world)

for countryName in world:
    print(countryName)
    stateMap = world[countryName]
    # print(stateMap)
    for stateName in stateMap:
        print("\t - " + stateName)
        cities = stateMap[stateName]
        for cityName in cities:
            print("\t \t - " + str(cityName))
