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












#
