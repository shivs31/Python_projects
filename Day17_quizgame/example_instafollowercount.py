# Example: Tracking instagram following and followers count

#creating class for users
class User:

    #creating attribute for the class(attribute is a variable associate with an object, similar like creating a new variable )
    def __init__(self, user_id, username): 
        self.id = user_id
        self.username = username
        self.followers = 0 
        self.following = 0

    #creating methods(function is attached to object is called method)
    def follow(self, user):
        user.followers += 1
        self.following += 1



# creating object from the class : instagram users
user_1 = User("001","shivani")
user_2 = User("002", "rekala")

user_1.follow(user_2)
print(user_1.followers) #account is 0
print(user_1.following) #following one account: user_2
print(user_2.followers) #has one follower: user_1
print(user_2.following) #user_2 is not following any account yet 