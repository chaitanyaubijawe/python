# Dynamic typing.
# python Variables.
#Number
a = 51234567890234567.11231
print(type(a))

print(a)

a = 1 + 1

a = 10 / 2
print(a)
a = 11 % 2

print(a)

a = 11 ** 2

print(a)


a = 1
# print(dir(__builtins__))

# String....
# sequences.
    # indexed.

s = "ABCD"
print(s)
print(s[1])

s = 'ABCD'
s = 'AB"CD'
s = "AB'CD"
s = "AB\"CD"

s = "ABCD" + str(1)

print("ABCD" + str(a))
print("ABCD" + str(1))
print(type(a))

s = "ABCDA" # s is ref variabl.

print(type(s))
print(s.count("A"))
print(s.count("B"))
print(len(s))

print(s.lower())

var_1 = "EFGH"

s = "ABCD - " + var_1
print(s)

s1 = "ABCD - {} "
s = s1.format("EFGH")
print(s)


s1 = "ABCD - {0} {1} "
s = s1.format("EFGH", "IJKL")

print(s)


s = "ABCD"
print("Before :: " + s)
print(s.replace("A","X"))
s = s.replace("A","X")
print("After :: " + s)



# Template...
s1 = "Name - {1} {0} "


s = s1.format("Surendra", "Soni")

print(s)

s = s1.format("Chaitanya", "Bijawe")
print(s)



s1 = "Name - {l_name} {f_name} "
s = s1.format(f_name="Surendra", l_name="Soni")
print(s)

# formatted string inside python version 3
f_name="Surendra"
l_name="Soni"

s1 = f"Name - {l_name} {f_name} "
s = s1.format(f_name,l_name)
print(s)


# string in immutable....
s = "ABC"

print(s[0])

# s[0] = "XX"


print(s)

# Boolean

b = False


print("Boolean :  " + str(b))


b = True


print("Boolean :  " + str(b))
print(type(b))

chaitanya = "this is variable...."
b = chaitanya

print(b)

b = True
n = 1 + b

print(n)



b = False
n = 1 + b

print(n)


# List ::

l = []
print(l)
l = list()
print(l)
l = [1,2,3]
print(l)
l = [1,2,3, "String1", "string2"]
print(l)
l = ["One",2,3, "String1", "string2", True, False]
print(l)

# Sequence.
print( "Zeroth Index :: "+ str(l[0]) )
print( "Forth Index :: "+ str(l[4]) )


# split slicing.

print(l[0:4])
print(l[:-4])

print( "Before " + str(len(l)))
# dynamic way of adding element to list.
l.append("Another element added here....")
l.append("Next ... Another element added here....")


print(l)


print( "After " + str(len(l)))

r = l[1]
print(r)

l[1] = "New value"
r = l[1]
print(r)
print(l)
# l[0]
# l[2]
# l[3]


for item in l:
    print( " Value is :: " + str(item))
# exit of loop


l1 = ["1", "123", "1234"]

print("Before " + str(l))
l.extend(l1)

print("After " + str(l))



print("Before " + str(l))
l.append(l1)

print("After " + str(l))

l = [4,1,2,3]
l = ["A","B","Z","C"]
print(l.sort())

print(l)

l.clear()
# l = []

print(l)


l = []

for item in range(1,10):
    print(item)
    l.append(item)
    # item = [1]
    print(type(item))
    # l.extend(item)


print(l)
v = l.pop()
print("Popped item is :: " + str(v))
print(l)
v = l.pop()
print("Popped item is :: " + str(v))

print(l)
# indexed element to be removed
v = l.pop(3)
print("Popped item is :: " + str(v))

print(l)
# actual value to be removed...
v = l.remove(1)
print("remove item is :: " + str(v))
print(l)


# tuple : bhai list ka..
# Immutable...

t = ()
t = tuple()
t = (1,3,4,5)
t = (1,3,4,"asdasd", "asdas")

# Accessing # reading.
print(t[0])

# t[0] = "1"
l = [ "one", "two" ]
# ref variable use....
t = (1,2,3, l)

# static allocation...
t = (1,2,3, [ "one", "two" ], 3)

l = t[3]# assign list to variable l.

print(type(l))

print(l)

l.append("three...")
print(l)
print(t)

print(t.index(3))

# if(current running time >> config.executionTimeoF ProgrM)



city_1 = "City_1"
city_1 = "City_1"
city_1 = "City_1"
city_10 = "City_10"

l = []

l.append(city_1)
l.append(city_1)
l.append(city_1)
l.append(city_10)

l = []
for item in range(1,11):
    city_name = "City_" + str(item)
    print(city_name)
    l.append(city_name)
print(l)

print("||".join(l))


''' document string in python ::
    City_1 || City_2...... || City_10
 '''

for item in l:
    print(item)


print("Abc", end="")
print(" - XYZ", end="")
print(" - PQR")


'''
*
* *
* * *
* * * *
* * * * *

1
1 2
1 2 3
1 2 3 4
'''


# print("Hello")

for repititions in range(3):

    for another in range(1,6):
        print("Internal :: hello")
    #print("upar wala...")
