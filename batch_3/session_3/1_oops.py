class Battery:
    materialOfBattery=""
    cellsOfBattery=0
    standByTime=0
    standByTimeUnit="seconds"

# Class in python.....
class Laptop:

    typeOfLaptop=""
    processor={}
    manufacturers=[]# list of comp names....

    battery=None




if __name__ == "__main__":
    # creating object of laptop class....
    notebook = Laptop()
    # before assigniong properties to object ::

    print("Type of laptop is ::" + notebook.typeOfLaptop)

    notebook.typeOfLaptop="Notebook Pro"

    notebook.processor={"core":8,"name":"OctaCore", "family":"i7"}
    notebook.manufacturers=["Dell", "HP"]
    print("Type of laptop is ::" + str(notebook.typeOfLaptop))
    print("processor of laptop is ::" + str(notebook.processor))
    print("manufacturers of laptop is ::" + str(notebook.manufacturers))


    # Assing battery to laptop...

    battery = Battery()
    battery.materialOfBattery="lithiumIonBattery"
    battery.cellsOfBattery=8
    battery.standByTime=8
    battery.standByTimeUnit="hours"


    notebook.battery = battery


    print("Battery material is ::" + notebook.battery.materialOfBattery)



    print(__name__)
