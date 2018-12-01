def m1():
    print("sdfsdf")
    a = 4
    b = 4

    return a + b


v = "asds"

print(v)

addition = m1()

print(v)
c = "string" + str(5)
print(c)

# List:
# how to define list
l = []  # empty List
l1 = [1, 2, 3]  # list with elements.
l3 = list()  # builtin function
t1 = (1, 2, 3)
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

c = [1, 2, 3]
l.append(c)

print("List after append :: ", l)
print("List after append size is:: ", len(l))

print("Splicing : ", l[2:])  ## elemenst AFTER 2 nd index will be printed....
print("Splicing : ", l[:2])  ## elemenst BEFORE 2(exclude) nd index will be printed....
## negative positions will start from -1(last index)


# add elements from other list to a existing list.

l.extend(c)

l.append(1)
print("List after append :: ", l)

## remove from List search for occurences and remove first .
l.remove(1)
## try del ??


print("List after REMOVING value :: ", l)

s = "MITESH"
l.extend(s)
l.append(s)

print("List after append :: ", l)
#   l.pop() ## by default remove element present at last index....
l.pop(2)  ## remove element present at 2nd  index....

print("List after pop :: ", l)
################################
# in operator...

a = 1 in l  ## return boolean value. True if found else false.

print("1 in l ::", a)

b = "I" in s
print("I in string ::", b)

# iteration...

for item in l:
    print("Items inside lists are: ", item)

for index, value in enumerate(l):
    print("Items inside lists with index are: ", index, value)

# range(1,100)

comp = [item * 2 for item in range(1, 200) if item % 2 == 0]
## [ element (operation) for element in iterable condition ]
print("Comprehessions :  ", comp)

l12 = []  # expressions...
for i in range(1, 200):
    print(i)
    l12.append(i)

print(l12)

new_copied_list = l12.copy()

print("Shallow copy of list : ", new_copied_list)

s1 = {1, 2, 3}
s2 = {5, 2, 7}

print(s1 & s2)

print(s1 | s2)

print(s1 ^ s2)
print(s1 <= s2)
print(s1 >= s2)

a = "6"
b = []

s = {1, 2}
l = [12, 23]
t = ()
t = (1, 2, 3)
t = (s)
t = (l)
print("tuple : ", t)
a = "7";

b.append(1)
print("tuple a= 7 ? : ", t)


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.__dict__)


p = Person("chaitanya")
# p.name = "chaitanya"
t = (p)
print("tuple Person: ", t)
p.name = "Mitesh"
print("tuple Person: ", t)

d = {"z1": "12313", "z2": "zzdsdsd"}

print("Keys are :: ", d.keys())
value = d["z1"]
print("z1 is key and its value in dict is :: ", value)

for key in d.keys():
    print("d[key]", d[key], " :: d.get(key)", d.get(key))

for value in d.values():
    print("iterating on values: ", value)

for key, value in d.items():
    print("Key is ", key, " value is :: ", value)

l = [["z1", "12313"], ["key_2", "value_2"]]

for ll in l:
    print("list inside list ", ll)

l1 = ["1", "2"]

v1, v2 = l1;

for key, value in l:
    print("key ", key, "value is:::: ", value)

#############################################

l = [1, 2, 3]

for item in l:
    print("item : ", item)

l = [[1, 2, 3]]

for item in l:
    print("item : ", item)

########################

d = {}
print("empty dict :: ", d)

d["US"] = "its is bc country"

print("US  dict :: ", d)
