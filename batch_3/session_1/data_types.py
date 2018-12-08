print("Hello world....")


# Variables...

a = "This is a variable....."


print(a)
# is for  commenting out your code....
# predefined function present in your python at runtime......
'''predefined function present in your python at runtime......'''
#print(dir(__builtins__))

print(id(a))
print(hash(a))
print(type(a))
###############################
# Data types::
#Numbers
## - int
## - float


a = 6
b = 10
# arithmatic operations....
add = a + b

print("Addition of two vars is :: " + str(add))
# modulous operator...
quotient = b % a

print(quotient)
# divide
divident = b / a
divident = b // a
# >
# <
# >=
# <=

print(b > a)
print(divident)
print(type(divident))

#############################

# String......

a = "this is a simple String..."
a = 'this is a simple String...'
a = 'this is a "simple" String...'
a = "this is a 'simple' String..."
b = " This is another string..."


concatenation  = a + b

print(concatenation)
print("This is inline " + " concatenation....." + concatenation)
useraName = "ABCDEFg"
# string is :: Sequence (indexing....)..... iterable...
print(useraName[0])
print(useraName[1])
print("iterable.....")
for char in useraName:
    print(char)

# () ::  meaning calling a functions/method....
print(useraName.lower())
print(useraName.upper())
print(len(useraName))
name = "Abhishek {} {} "
# name = "Abhishek {1} {0} "
name = "Abhishek {surname} {occupation} "
print(name.format(surname= "Tomar", occupation=" is a Scientist....."))

srName = "Tomar....."
ocptn = " Scientist...."
# formatted string:: 3.7.##
name = f"Abhishek {srName} {ocptn}"
print(name)



# operator :: in

value = "A" in name
print(value)
value = "B" in name
print(value)
value = "X" in name
print(value)

## List...

# - container.....
# - it can hold dynamic range of elements...
#definition....
l = list()
l = []

l = ["one", "two", "three", 1, []]
# accessing 0th postional element....
print(l[0])
l[0]= 1
print("##########")
for item in l:
    print(item)


l.append("another element")
l.append("another item")
l.append(0)
l.append([])

l.pop(0)
l.clear()
print("##########")

for item in l:
    print(item)

# tuple::

t = ()
t = (1,2)
t = tuple()
t = (1,2,4, ["one","two"])


print(t[0])

#t[0] = "ONE" ## not allowed.... immutable....


l = t[3]

l.append(123132)

print(t)


for item in t:
    print(item)


# Dictionaries...

# key: value
# it cannot hold duplicate key..
d = {}
d = {"key":"value","key_2":"value_2"}
d = {"key":"value","key_2":[123,1231], "key_3":(12,12,12)}

print(d["key"])
v = d["key"]

d["key"] = "asdfasadas"
print(v)
for key in d:
    print(key)


for key in d:
    print(key  + " ---- " + str(d[key]))


print(type(d.keys()))

for key in d.keys():
    print(key  + " ---- " + str(d[key]))

print(type(d.items()))

for key,value in d.items():
    print(key  + " ---- " + str(d[key]))


for thing in d.items():
    print(thing)



# Set

s = {}
s = {"a", 2, 6,1}
# unique elements..
# Exercise operators for set... union intersection etc...
# you cannot access set element bby using index.... s[0] will result error

print(s)
for elem in s:
    print(elem)
# World Map : gather country/state/cities....
