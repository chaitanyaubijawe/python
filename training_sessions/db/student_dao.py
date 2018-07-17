def insert_student_random(number=10):
	for num in range(10):
		query = "INSERT INTO student (id, name, age) VALUES("+ str(num) + ", 'name_" + str(num) + "', "+ str(num) +"); "
		print( query)
	for num in range(10):
		query = "INSERT INTO student (id, name, age) VALUES({}, 'name_{}', {});".format(num, num, num)
		print( query)


#insert_student_random(10)

def update_student_dict(projection={}):
	query = "UPDATE student set "
	for key in projection.keys():
		if key == 'id':
			continue
		if key == 'name':
			query += key + " = '" + projection[key] + "', "
		else:
			query += key + " = " + str(projection[key])
	query = query[:-1]
	where_clause = " where id = " + str(projection['id'])
	query += where_clause
	print( query)

#update_student_dict({'id':1, 'name':"updated_name_24", 'age':24})
#update_student_dict({'id':25, 'name':"updated_name_25", 'age':25})

def insert_student(projection={}):
	query = "INSERT INTO student (id, name, age) VALUES("

	for key in projection:
		query += str(projection[key]) + ","

	query = query[:-1] + "); "
	print(query)

#insert_student({'id':1, 'name':"updated_name_24", 'age':24})
#insert_student({'id':3, 'name':"updated_name_345", 'age':34})
