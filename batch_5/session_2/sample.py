import collections


def m():
    print("m")

a = collections.namedtuple("Emp", "name, age")


print(a)
print(a.name)
