def get_cities(country, state):
    cities = []
    # COUNTRY_NAME_STATE_City
    for counter in range(5):
        cityName = country + "_" + state + "_" + "city_" + str(counter)
        cities.append(cityName)

    # to fetch data from DB....
    # fetch it from file...
    return cities


def get_state_map(countryName):
    stateDict = {}
    # {"MAh":["cities1", "city2"]}

    ## if blocks....
    if (countryName == "IND"):

        stateDict["MAH"] = get_cities(countryName, "MAH")
        stateDict["MP"] = get_cities(countryName, "MP")
    elif(countryName == "USA"):
        stateDict["CT"] = get_cities(countryName, "CT")
    else:
        pass

    return stateDict


# print(get_state_map())


def world_map():
    world_map = {}

    world_map["IND"] = get_state_map("IND")
    world_map["USA"] = get_state_map("USA")
    return world_map


print(world_map())
