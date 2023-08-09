class User : 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def introduce(self):
        print(self.username)

user_1 = User("michael", 1234)
user_2 = User("mike", 894305)

user_1.introduce()
user_2.introduce()

