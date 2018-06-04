def m1():
	return 2;


s1 = "codesnbugs"


print(s1[0])
print("length :", len(s1))

print("slicing ", s1[m1():])
print("slicing s1[1:5] ", s1[1:5])







s1 = {1,2,3}
s2 = {5,2,7}

print (s1 & s2)

print (s1 | s2)


print (s1 ^ s2)
print (s1 <= s2)
print (s1 >= s2)
