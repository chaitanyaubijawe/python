class ServerInfo:

    os = None
    def __init__(self, name):
        # called automaticlally... when insta(nce is created...
        print("This is constructor...." + str(self))
        self.name = name
        self.__privateVar = "this is convention for private method..."

    def getNameOfServer(self):
        print("inside getNameOfServer :: " + str(self))
        return self.name

    def __privateMehtod(self):
        print("inside getNameOfServer :: " + str(self))
        return self.name

    @classmethod
    def getCV(cls):
        return cls.os

    # hack... dont follow this...
    def getCV_V(cls):
        return cls.os

    @staticmethod
    def getCurrentTime():
        import datetime
        return datetime.datetime.now()


if __name__ == "__main__":

    # accessing class level variable.... by using Class Name
    ServerInfo.os = "Linux...."

    print("Access class method:: " + ServerInfo.getCV())
    # hack... dont follow this...
    print("Access class method:: " + ServerInfo.getCV_V(ServerInfo))
    print("Access class method:: " + str(ServerInfo.getCurrentTime()))
    s = ServerInfo("Dell")
    #s.name = "Dell"

    print("OS:: class level variable :: ", ServerInfo.os)
    print("NAME:: instance  variable :: ", s.name)
    print("NAME:: instance  method :: ", s.getNameOfServer())

    s2 = ServerInfo("HP")
    #s2.name = "HP"
    s2.os = "UBUNTOO"
    #ServerInfo.os = "UBUNTOO"


    print("OS:: class level variable :: ", ServerInfo.os)
    print("OS:: class level variable :: ", s2.os)
    print("NAME:: instance  variable :: ", s2.name)
