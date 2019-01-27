# print("Hello !")


 # Dynamically datatyped  language...



# Datatype....

print("Hello")
# Number
    # 1- int.
    # 2- float.
var_1 = 1


print(var_1)
print(type(var_1))

var_1 = 1.1


print(var_1)


print(type(var_1))



var_2 = 1
var_3 = 2
 # arithmatic operations...
add = var_2 + var_3
add = var_2 + var_3
add = var_2 / var_3
add = var_2 - var_3
add = var_2 % var_3
# add = function call.
# add = object creation
# add = any python expression....

print(var_2 + var_3)

print(add)


# String...
s = "abc"
s = "a\"b\"c"
s = 'abc'
s = 'a"b"c'
s = 'a\'b\'c'


s = "a'b'c"

# string in python is sequence..... of characters....
# u can access characters by its index....
# string is immutable.... means it is final.. u cannot change it...

print(s[0])
print(s[1])
print(s[4])



char_at_0 = s[0]

print(char_at_0)

# s[0] = "M"
# char_at_0 = s[0]
#
# print(char_at_0)





s = "MBA"
# 01234
#-5-4-3-2-1



print(s.lower())
print(s.upper())
print(s.count("a"))
print(len(s))
# slicing....
# print(s[0:2])
# print(s[-5:])

n = "Mahendra Nikam is "
name =  n + s + " and a financial analyst"
nm = "Mahendra Nikam is {0} and studied {1}"
name = nm.format("financial analyst", "MBA")

print(name)


nm = "Mahendra Nikam is {job} and studied {education}"
name = nm.format(job = "financial analyst", education="MBA")

print(name)


job = "Financial analyst"
education = "MBA"

# Python 3. Formatted string....
nm = f"Mahendra Nikam is {job} and studied {education}"

print(nm)


num = 1
s = "one: " + str(num)


print("ABCD" + str(1))
print("ABCD" + str(num))



nm = "NAME"

for character in nm:
    print(character)

#Exercise.....
# "NAME_1"
# "NAME_2"
# "NAME_3"
# "NAME_4"

# num_1 = 1
# num_2 = 2
# num_3 = 3
# num_4 = 4
# print("NAME_"+str(num_1))
# print("NAME_"+str(num_2))
# print("NAME_"+str(num_3))
# print("NAME_"+str(num_4))


num = "1234"

for character in num:
    print( "NAME_" + character)

print("first line", end=" ")
print("Second line")




#*
#* *
#* * *
#* * * *


#1
#1 2
#1 2 3
#1 2 3 4


r = range(5)

print(r)

# for num in range(5):
for num in r:
    print ("Name_" + str(num))



for num in r:
    for num_2 in r:
        print("1")
    print()



shoes_1 = "1"
shoes_2 = "2"
shoes_3 = "3"
shoes_4 = "4"


print(shoes_1)


l = []
l = [1,2,3]
l = ["string", 123, "asdfasd"]
l = ["string", 123, "asdfasd", []]
l = ["string", 123, "asdfasd", shoes_1, shoes_2]
# empty list....
l = list()

l.append(1)
l.append("2")
l.append("three")
l.append([])




print(l)
l.pop()
print(l)
# l.pop(1)
# print(l)


elem_1 = l[0]
elem_2 = l[1]

print(elem_1, elem_2)


# adding an element to list :: append.
# accessing an element is l[0] [index position should go here...]...... if index not present, it will throw error.
# for loop.


for element in l:
    print(element)

# help(list)
# help(str)


l.clear()

print(l)


print("*")
