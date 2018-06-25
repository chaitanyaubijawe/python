

def m1():
    print("sdfsdf")
    a= 4
    b = 4

    return a+b

v = "asds"

print(v)

addition = m1()

print(v)
c= "string" + str(5)
print(c)

# List:
# how to define list
l = [] # empty List
l1 =[1,2,3] # list with elements.
l3 = list() #  builtin function
t1 = (1,2,3)
l4 = list(t1)

print("List :: ", l)
print("List with elements :: ", l1)
print("List with builtin function:: ", l3)
print("List with tuple :: ", l4)

# how to add elements in a list.

# append...

l.append("PB")
l.append("CB")
l.append("MJ")

a = "abc"
# l is ref variable of type list.
l.append(a)

b = 4
l.append(b)

c = [1,2,3]
l.append(c)


print("List after append :: ", l)
print("List after append size is:: ", len(l))


print("Splicing : ", l[2:]) ## elemenst AFTER 2 nd index will be printed....
print("Splicing : ", l[:2]) ## elemenst BEFORE 2(exclude) nd index will be printed....
## negative positions will start from -1(last index)


# add elements from other list to a existing list.

l.extend(c)

l.append(1)
print("List after append :: ", l)

## remove from List
l.remove(1)
## try del ??


print("List after REMOVING value :: ", l)


s = "MITESH"
l.extend(s)
l.append(s)

print("List after append :: ", l)
#   l.pop() ## by default remove element present at last index....
l.pop(2) ## remove element present at 2nd  index....

print("List after pop :: ", l)
################################
# in operator...

a = 1 in l ## return boolean value. True if found else false.

print("1 in l ::", a)

b = "I" in s
print("I in string ::", b)

# iteration...

for item in l:
    print("Items inside lists are: ", item)


for index, value in enumerate(l):
    print("Items inside lists with index are: ", index, value)

# range(1,100)

comp =[ item*2 for item in range(1,200) if item % 2 == 0]
## [ element (operation) for element in iterable condition ]
print("Comprehessions :  ", comp)

l12 =[]
for i in range(1,200):
    print(i)
    l12.append(i)

print(l12)
