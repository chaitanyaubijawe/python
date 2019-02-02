t=()
t=tuple()
t=(1,2,3,1, ["a","b"])

#IMMUTABLE. FINAL


print(str(t[0]))
print(t.count(1))
print(t.index(2))

# t[0] = "updated......"

list_inside_TPL = t[4]


print("Before:: "+str(list_inside_TPL))

list_inside_TPL.append("abcd")

list_inside_TPL[1]="asdasdasd"
list_inside_TPL[2]="replaced__abcd...."

print("After:: "+str(list_inside_TPL))

print(t)


# Dict
# key value pair....
# key can be e.g. string integer.


# key cannot be null None.
# value can be anything : Strubng, numbers, list, dictionary, python custom object.
# duplicate keys are not5n allowed.
#

d = dict()
d = {}
d = {"key":"value" }

k  = "key"
print(d[k] + " -ABCD- " + d.get(k))

d["key_2"] = "Value_2"

print(d)


d["key_2"] = "Value_3"


d[None] = "Value_4"
d[None] = "Value_5"

# dict inside dict....
d["another_dict"] = {"insider":"value"}
d["another_list"] = ["insider","value"]
print(d)

#Dynamically acceessing dictionary.
for k in d:
    # k  = "key"
    print(str(k) + " -- "+ str(d[k]) )

print("$$$$$$$$$$$")
for k in d.keys():
    print(k)

print("$$$$$$$$$$$")
for k,v in d.items():
    print( str(type(k)) + " --" + str(k) + " -- " + str(v) + " -- " + str(type(v)))


# Student
# NAME
# Age
# Standard

#Address:
    # - ["Banyan tree society7, tuykaram nagar... pin code", "office aaddrr..."]
    # - [{"addr_line_1":"line 1", "addr_line_2":"line 2", "pin_code":"234234", "road":""}, {}]
