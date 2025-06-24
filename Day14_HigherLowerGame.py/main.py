import random
from game_data import data
#Display logo
from art import logo, vs


#extracting data count & display name, description , country
def format_data(account):
    """ Format the account data and return printable format. """
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, {account_description}, {account_country}"

# Compare the followers count and return
def check_answer(user_guess, a_followers, b_followers):
    """ Take a user's guess and the follower counts and returns if they got it right """
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


print(logo)        
score = 0

# Generate 'A' random account from the game data
account_A = random.choice(data)

#Make the game repeatable.
game_should_continue = True


while game_should_continue:

    #making account at position B become the next account at position A
    account_B = random.choice(data)
    account_A = account_B
    

    if account_A == account_B:
        account_B = random.choice(data)


    print(f"Compare A :{format_data(account_A)}")

    #display vs

    print(vs)

    print(f"Against B : {format_data(account_B)}")
        

    #Ask user to guess 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    #Clear the screen
    print('\n' * 20)
    print(logo) 

    #Check if user is correct
    #-Get followers from each account to compare
    a_follower_count = account_A['follower_count']
    b_follower_count = account_B['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #if correct give feedback 
    #score keeping
    if is_correct:
        score += 1
        print(f"You are right! Correct Score: {score}")
    else:
        print(f"Sorry! you are wrong. Final Score: {score}")
        game_should_continue = False

