'''
youre to create a calculator app 
users have to use it by inputing a username 

the users than can use it are ['michael', 'victor', 'emmanuel']
you ask for thier ages , if users age is greater than 18 :
they can proceed - you ask them to input the two variables 
a and b 
you ask what operation they want to perform - "add", "sub", "mul", "div"

users can "Add" , "subtract", "divide", "multiply"
you use if and elif and else statement to perform the four 
and return anyone the user selects 
'''
a = input()
b = input()
operation = input("what operation do you want (add , mul, sub, div) : ")
if operation  == "add" : 
    sum = (a+b)
    print(sum)

    