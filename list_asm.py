users = [] #empty list

# user_instance = {
#     "username" : "dummy_username",
#     "password" : "dummy_password"
# }

username = str(input("Enter your username : "))
password = str(input("Enter password"))

instance = { 
    "username" : username,
    "password" : password
}

users.append(instance)
print(users)
