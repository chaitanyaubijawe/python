def parent_method(arg):

    def m1():
        print("Inside m1 :: ", arg)
    def m2():
        print("inside m2 :: ", arg)

    m1()
    m2()

#parent_method("this is argument...")


w_map = "this is global"

def parent_method_keyword(arg):

    def m0():
        # method local variable.....
        w_map = "Method local variable..."

    def m1():
        #nonlocal w_map
        w_map = "non local scope assigning inside method...."

    def m2():
        global w_map
        w_map = "global scope is assinged....."


    # w_map = "This is method variable"
    # print("before W_map :: ", w_map)
    # m0()
    # print("after assigning value in local method.... W_map :: ", w_map)
    # m1()
    # print("after assigning value with nonlocal keyword.... W_map :: ", w_map)
    global w_map
    m2()
    print("after assigning value with global keyword.... W_map :: ", w_map)

#print("Golbal W_map :: ", w_map)
parent_method_keyword("this is argument...")
#print("Global keyword.... W_map :: ", w_map)
# city_1 = "city_1"
# city_2 = "city_2"
# city_3 = "city_3"
# cities = []
# userInput = 5
# for number in range(userInput):
#     city = state_name + "_" + str(number)
#     print("generated city is :: ", city)
#     cities.append(city)
#
# for city in cities:
#     print("City inside list is ", city)

def populate_and_get_city_by_state(state_name, range_value):
    cities = []

    for number in range(range_value ):
        city = state_name + "_" + str(number)
        print("generated city is :: ", city)
        cities.append(city)
    return cities

cities = populate_and_get_city_by_state("Mah", 30)

for city in cities:
    print("City inside list is ", city)
insert_query = "INSERT INTO student(id, name, age) VALUES (1,'{}', 1)".format("name_1"


print (insert_query)
