class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        User.total_users +=1

    def get_info(self):
        return (self.username,User.total_users)

user1 = User("alice")
user2 = User("bob")
print(user1.get_info())
print(user2.get_info())