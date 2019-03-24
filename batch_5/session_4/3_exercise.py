class Exercise:

    def __init__(self):
        print("Inside constructor.....")

    def getCities(self, stateName):
        '''this will return list of random cities....'''
        cities = []
        print("Inside getCities.....")
        for i in range(1,6):
            rs = stateName + "_CITY_" + str(i)
            cities.append(rs)
        print("#CITIES#DONE#")
        return cities

    def getStateData(self, *args):
        print("Inside getStateData.....")
        stateMap = {}
        for state in args:
            cities = self.getCities(state)
            stateMap[state] = cities
        return stateMap

    def getWorldData(self):
        print("Inside getWorldData.....")
        worldMap = {}
        stateMapInd = self.getStateData("MAH", "MP","UP")
        worldMap["IND"] = stateMapInd
        stateMapUS = self.getStateData("CT", "ABC","DHIKANA")
        worldMap["US"] = stateMapUS
        return worldMap

    @staticmethod
    def printData(world):
        for countryName in world:
            print(countryName)
            stateMap = world[countryName]
            # print(stateMap)
            for stateName in stateMap:
                print("\t - " + stateName)
                cities = stateMap[stateName]
                for cityName in cities:
                    print("\t \t - " + str(cityName))


if __name__ == "__main__":
    exercise = Exercise()
    data = exercise.getWorldData()
    Exercise.printData(data)
    # print(data)
