# Dictionaries...

d = {}
d = dict()
d = {"key":"value...."}
d = {"key":[]}
d = {"key":()}
d = {"key":{}}


d = {"key":"value_1", "key_2":"value_2"}


# add more keys and values...

d["key_3"] = "value_3"
print("Before::::: ")
print(d)

print("After::::: ")
d["key_3"] = "value_3sdfsdfsd"

# access or reading a particular key...
value = d["key_2"] # value_2


print(d)


for key in d:
    print(key + "-------" + d[key])


print(type(d.keys()))
for key in d.keys():
    print( "Using keys method....."+ key)

print(type(d.values()))

for value in d.values():
    print( "Using values method....."+ value)

print(type(d.items()))

for key,value in d.items():
    print( "Using items method....."+ key + " ------ " +  value)


print(type(enumerate(d)))
for key, value in enumerate(d):
    print(key, value)


l1 = ["value _1", "calue_2"]
l2 = ["value _3", "calue_4"]


print(zip(l1,l2))


# Tuple::

t = ()
t = tuple()

l = ["one", "two", "threee...."]

v = [l[0]]


print("BEFORE : accessing v:: " + v[0])

v[0] = "ONE"

print("AFTER : accessing v:: " + v[0])
print("AFTER : accessing L :: :: " + l[0])


t = (1,2,3 , ["1","2"])


# print("before...")
# print(t)
# immutable....

listInsideTpl = t[3]

#t[3] = ["zsfasd"]


listInsideTpl.append("3")
listInsideTpl.append("4")


print(listInsideTpl)
print(t)





l = ["1", "2", ["ONE", "TWO"]]

listInsideList = l[2]
listInsideList.append("Three......")

print(l)





ll = ["ONE", "TWO"]

def m(l):
    l = ["qweqwe", "qweqsdxzdf"]
    return l




print(m(ll))
ll = m(ll)
print(ll)



def m2(l):
    l.append("another value")
    l.append("again....another value")


m2(ll)


print(ll)



# SET
s = {}
s = set()
s = {2,3,1,5, "a"}


print(s)


for elem in s:
    print(elem)


# Boolean

b = True
b = False
