class Processor:
    core=None
    name=None
    family=None


class Memory:
    size=None
    availableMem=None

class ServerInfo:
    os=None# string....
    serverType=None#string
    processor={}
    eth=[]
    memory=None




if __name__ == "__main__":
    # creating object of a class...
    linuxServer = ServerInfo()
    # linuxServer is ref variable.....
    #  object instantiation....

    print("Before setting anythin :: " + str(linuxServer.os))
    linuxServer.os= "REDHAT"
    linuxServer.serverType= "DELL"
    linuxServer.processor= {"core":"8","name":"octacore","family":"i7"}
    linuxServer.eth = ["eth0", "eth1"]
    print("after setting os :: " + linuxServer.os)
    print("after setting serverType :: " + linuxServer.serverType)
    print("after setting processor :: " + str(linuxServer.processor))
    print("after setting eth :: " + str(linuxServer.eth))
    print("after setting eth :: " + str(linuxServer.__dict__))

    memory = Memory()
    memory.size = 128
    memory.availableMem = 100

    linuxServer.memory = memory

    print("Memory :: " + str(linuxServer.memory.size))
    print("Memory :: " + str(linuxServer.memory.availableMem))
