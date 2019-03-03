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
