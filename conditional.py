age = int(input("Enter your age  : "))
if age > 17 : 
   location = str(input("Enter your location : "))
   if location == "lagos" or "abia":
        print("User has registered successfully")
   elif location == "abuja":
        print("user can register nextweek") 
   elif location == "portharcourt" : 
        print("Users can register tomorrow ")
   else :
        print("people in your location cannot register")
else :
    print("X is less than 5 ")
