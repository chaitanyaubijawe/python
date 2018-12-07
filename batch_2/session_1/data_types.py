print("hello world.l...")
# builtin functions
# print(dir(__builtins__))

# ##  DATA Types::
#
# #Number
#     - int
#     - float
#     - long
# # String
#     - ""
#     - ''
# # List
#     - Ordered
# # Tuple
#     - immutable
# #Dict
#     - {key:value}
# # SET
#     -Sorted...
# #Boolean...
#  - True
#  - False


a = 5234567834567856234567890 # int long
#dynamic typing....
# variable == a
# operator => =
# number = 5
print(a)
print(type(a))


a = 3*5
print(4+5)


# %

a = 5/2

print (a)

# String
# sequences...
a = "this is simple string......"
b = 'another string....'
result = a + b
#result[0] = "ABC" # immutable
print(result[0])


a = "This is a  {1} {1}".format("simple script...", "another input.....")
a = "This is a  {a} {s}".format(s= "simple script...", a="another input.....")

print(a)
aa = "simple script...."
a = f'This is  {aa} ' ## F - string....

print(a)


# List

l = list()
l = [1,2,3]
l = []

# methods
l.append(2)

ll = [1,2,4]

result_boolean = 4 in ll

result = l + ll
print(result)
l.extend(ll)

## indexing

print(l[0])
print(l[2])

# Slicing

print(l[::])
print(l[2::])
print(l[:4:])

l.pop()


for item in ll:
    print("Items inside list :: " + str(item))


# list comprehension
range(1,10) ## 1-9 digits.....

length = len(ll)

for i in range(0,length):
    print(ll[i])


# ll = [expressions : for loop: contions...true n false ]

l_comperhension = [ item * 2  for item in range(100) if item % 2 == 0 ]
