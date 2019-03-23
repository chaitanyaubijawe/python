a = 5
b = 6
sum = a + b
print(sum)

def m():
    a = 6
    b = 7
    sum = a + b
    print(sum)
m()


def m1(arg_1, arg_2):
    a = arg_1
    b = arg_2
    sum = a + b
    print(sum)

m1(1,2)
m1(1,4)
m1(1,6)


def m2(arg_1=1, arg_2=1):
    a = arg_1
    b = arg_2
    sum = a + b
    print(sum)
m2()
m2(1,2)
m2(arg_1 = 1, arg_2 = 2)
m2(arg_2 = 2)
m2(arg_1 = 2)

def m3(arg_1, arg_2=1):
    a = arg_1
    b = arg_2
    sum = a + b
    print(sum)
m3(1,2)



def m4(arg_1, arg_2, arg_3):
    a = arg_1
    b = arg_2
    c = arg_3
    sum = a + b + c
    print(sum)
m4(1,2,3)



def m5(*args):
    print(type(args))
    print(args)
    sum = 0
    for item in args:
        sum = sum + item
    print(sum)

m5(1,2,3,1,3)


def m6(**args):
    print(type(args))
    print(args)

    for key in args:
        print("KEY is :: " + str(key) + " --- "  + str(args[key]))

m6(a=1,b=2,name=3,falana=1,xyz=3)




# getting toothpaste = 40
# getting brush = 50

# surendra braught saman  = 400

surendra_amnt = 400

def m7(*args):
    print(type(args))
    print(args)
    sum = 0
    for item in args:
        sum = sum + item
    return sum

chaitanya_amnt = m7(10,20,30,10,30)

total_kharcha = chaitanya_amnt + surendra_amnt

print(total_kharcha)


print("------------------------------")
print("------------------------------")
print("------------------------------")

# mi tv
# amazon
#     - Electronics
                # -[]
#Electronics_Product_1
ecom = {"amazon":{  "Electronics":["MI TV", "Phone Apple", "Apple laptop"],"books":["Harry potter", "ABC", "science"] }}

def getProducts(category):
    l = []
    for item in range(5):
        name = category + "_Product_"+str(item)
        l.append(name)
    return l




def getCategoryData(*args):
    d = {}
    # electronis_products = getProducts("Electronics")
    # d["Electronics"] = getProducts("Electronics")
    # d["Books"] = getProducts("Books")
    # d["Automobile"] = getProducts("Automobile")

    for category in args:
        d[category] = getProducts(category)
    return d


def getEcomData():

    ecomData = {}
    ecomData["Amazon"] = getCategoryData("Electronics","Books")
    ecomData["Flipkart"] = getCategoryData("Automobile")
    ecomData["Myntra"] = getCategoryData("Clothing")
    return ecomData


data  = getEcomData()

print(data)

print("------------------------------")

for ecomSite in data:
    print(ecomSite)
    siteData = data[ecomSite]
    for category in siteData:
        print("\t " + str(category))
        for product in siteData[category]:
            print("\t\t " + str(product))
print("------------------------------")

print(data["Amazon"]["Electronics"][:3])
print(data["Flipkart"]["Automobile"][:2])
print(data["Myntra"]["Clothing"][:4])
