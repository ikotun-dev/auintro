username = str(input("Enter your username : "))
if username == "michael" or username == "victor" or username == "emmanuel": 
    print("Login successful")
    age = int(input("Enter your age : "))
    if age > 18 :
        a = float(input("Enter the first number : "))
        b = float(input("Emter the second number : "))
        operation = str(input("Enter your operation : "))
        if operation == "add" : 
            add = str(a+b)
            print("The sum : " + add)
        elif operation  == "sub" : 
            sub = str(a-b)
            print("The difference is : " + sub)
        elif operation == "mul" : 
            mul = str(a*b)
            print("The multiplication is : " + mul)
        elif operation == "div" : 
            div = str(a/b)
            print("The division is : " + div)
    else : 
        print("Your age cannot perform this operation")
else : 
    print("users with this username cannot use this app")

