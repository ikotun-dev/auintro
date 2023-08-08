animals = ['dog', 'cat', 'horse', 'cow', 'sheep']

user_choice = str(input("Do you want to add or remove from the list"))
if user_choice == "add" : 
    new_car = str(input("Enter the new car name  : "))
    animals.append(new_car)
elif user_choice == "remove" : 
    print(animals)
    car_to_remove = str(input("Enter the car name to remove"))
    animals.remove(car_to_remove)
else : 
    print("othing here") 

# new_animal_1 = str(input("Enter your fist animal : "))
# new_animal_2 = str(input("Enter your second animal : "))

# animals.append(new_animal_1)
# animals.append(new_animal_2)

# animals.pop() # --> removes by index 

#animals.remove('cat') # ---> removes by data itself

#print(animals[0])
print(animals)

#print(type(animals))
