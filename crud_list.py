users = ('vitor', 'collins', 'emma') #our user list --> tuple 
list_of_posts = ['the sky is blue', 'lagos is a city', 'i have a watch'] #our lists of posts

username = str(input("Enter your username : "))
if username not in users : #if statement to check is user is present 
    print("User not found")
else : 
    print("Welcome " + username + "," + "what do you want to do? : ")
    print("1. Create posts")
    print("2. read posts ")
    print("3. delete posts ")
    option = int(input("Please enter the id of your option (eg : 2 -> for read posts)"))
    if option == 1 : 
        print("--Create Post--")
        new_post = str(input("Enter new post : "))
        list_of_posts.append(new_post)
        print("----post has been created successfully---")
        print(list_of_posts)
    elif option == 2:
        print("----List of Posts-----")
        for x in list_of_posts:
            print(x)
    elif option == 3 : 
        print("--Delete post--")
        print(list_of_posts)
        post_to_delete = str(input("Enter post to delete"))
        list_of_posts.remove(post_to_delete)
        print("Post has been deleted")
        print(list_of_posts)
    else : 
        print("This choice is not available")
        

  

