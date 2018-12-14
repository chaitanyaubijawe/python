user = {"name":"Abhisheklllll", "age":25}
user2 = {"name":"Chaitanya", "age":29}
user3 = {"name":"Abhishek", "age":29}


##input is list...
users = []
users.append(user2)
users.append(user)

users.append(user3)

#[{"name":"Abhishek", "age":25}]
#print(users)
#
# user = {}
# for u in users:
#     # print(u["name"])
#     if u["name"] == "Abhishek":
#         print("Printing information for abhishek......")
#         user = u
#     else:
#         print("User not found")

def findUser(name, users):
    user = {}
    for u in users:
        # print(u["name"])
        if u["name"] == name:
            print("User found.... ......")
            user = u
            break
        else:
            print("User not found")
    return user


print(findUser("Chaitanya", users))
print(findUser("Abhishek", users))
print(findUser("falana....", users))

print(findUser("Dhinkana", users))
