# Dictionary.
d = {}
d = dict()
d = {"key_1":"Value_1", "key_2":"value_2"}

print(d)


value = d['key_1'] # passed a key and taken valiue against that key...

print(value)

l = [1,2 ,43]
value = l[2]# index position. : value agaisnt that index...


d['key_3'] = "New value..."

print(d)


d['key_3'] = "Another New value..."

print(d)


# Accessing over for loop.

for key in d:
    print(str(key) + " -- " + str(d[key]) )


print(d.keys())
print(type(d.keys()))

for key in d.keys():
    print(str(key) + " -- " + str(d[key]) )

for key in d:
    print(str(key) + " -- " + str(d[key]) )


print(d.values())


for value in d.values():
    print(value)

print(d.get('key_1'))

d.clear()


message = {"data":"Hi there!", "type":"text", "to":"Shivam<89812312>", "from":"Surendra<868678>"}

building = {"floor":"4", "commercialSpaces":"5", "residential":"4" }


laptop = {"processor":"i7", "manufacturer":"mac", "os":"macos"}

# contacts =
student = {"name":"Chaitanya Bijawe", "age":30, "contacts":

[
{
"tag":"Personel",
"number":"8983237271"
}
,
{
"tag":"Official",
"number":"1234567890"
}
]
}


print(student)
studentsList = student['contacts']
print(studentsList)
print("&&&&&&&&&&&&&&&&&&&")
for item in studentsList:
    print(item)
    print(item["tag"])
print("&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&")

# set
# unique elements....

s = {}
s = set()
s = {1,2,34,4,2,1}

l = [1,2,3,4,1]
print(l)

s = set(l)
print(s)

s.add(5)
s.clear()
##########data types ends here....########
