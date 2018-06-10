def m1():
	return 2;


s1 = "codesnbugs"


print(s1[0])
print("length :", len(s1))

print("slicing ", s1[m1():])
print("slicing s1[1:5] ", s1[1:5])


s1 = {1,2,3}
s2 = {5,2,7}

print (s1 & s2)

print (s1 | s2)


print (s1 ^ s2)
print (s1 <= s2)
print (s1 >= s2)




''' Write a program to give Data of country '''

#India state lists.
mah_list = ["Pune", "Mumbai"]
mp_list = ["Indoor", "Jabalpur"]

#US state lists.
ct_list = ["Danbury"]


def get_city_list_by_state(arg=None):
	if arg == 'MAH':
		return mah_list
	elif arg == 'MP':
		return mp_list
	elif arg == 'CT':
		return ct_list

def populat_map_data():
	map = {}
	
	mah_list = get_city_list_by_state('MAH')
	mp_list = get_city_list_by_state('MP')

	india_state_map = {}
	india_state_map["MAH"] = mah_list;
	india_state_map["MP"] = mp_list;

	map["INDIA"] = india_state_map
	return map


map = populat_map_data()

for value in map:
	print("Country" , value)
	state_map =  map[value]
	for state in state_map:
		print("\t State : ", state)
		if state == 'MAH':
		    print("\t Not printing : ", state)
		    continue
		cities = state_map[state]
		for city in cities:
		 	print("\t\tCity : ", city)
		 	break
