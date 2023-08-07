import math
username = str(input("Enter your username : "))
if username == "michael" or username == "victor" or username == "emmanuel": 
    print("Login successful")
    age = int(input("Enter your age : "))
    if age > 18 :
        operation_type = int(input("enter 1 for operation with 1 number , 2 for 2 numbers : "))
        if operation_type == 2 : 
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
        elif operation_type == 1 : 
            b = float(input("Emter the second number : "))
            operation = str(input("Enter your operation (sin/cos/tan/sqr/root) : "))
            if operation == "sin" : 
                value = math.sin(math.radians(b))
                print("The sine is " + str(value))
            elif operation == "cos" : 
                value = math.cos(math.radians(b))
                print("The cosine is " + str(value))
            if operation == "tan" : 
                value = math.tan(math.radians(b))
                print("The tangent is " + str(value))
            if operation == "sqr" : 
                value = math.sqrt(b)
                print("The squareroot is " + str(value))
    else : 
        print("Your age cannot perform this operation")
else : 
    print("users with this username cannot use this app")
