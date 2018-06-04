print ("hi")
def m1():
    print("inside m1")
print ("hi after a method..")

x = 2
y = 3

arr = [4,1,2,3]
print("adding two string variable " + str(x+y))
m1()

def m2(a,b):
	print ("inside m2 adding them : " + str(a+b))

m2(1,2)


print(sorted(arr))

x= "2"
print(type(x))
print(id(x))



t=()
u=()

print(id(t))
print(id(u))



s1 = "at"
s2 = "at"

print(s1==s2)


class Basic:
	def m1(self):
		print("basic m1")
b =  Basic();
b.m1()
