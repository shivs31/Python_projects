import random

#global variables
EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0

#Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer,turns):
    """
    Checks num against guess, returns number of attempts remaining.
    """    
    if user_guess>actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess<actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it. The number is {actual_answer}")



#Function to set difficulty
def diff_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if difficulty == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1,100)

    #choose difficulty 
    turns = diff_level()
    

    
    #Repeat the guessing functionality if they get it wrong.
    
    num_guess = 0
    while num_guess!=num:
        
        print(f"You have {turns} attempts remaining to guess the number") 
        #Let the user guess the number
        num_guess = int(input("Make a guess: "))
        turns = check_answer(num_guess, num, turns)
        
        #Track the number of turns and reduce by 1 if they get it wrong

        if turns == 0:
            print("You have run out og guesses, you lose")
            return
        elif num_guess != num:
            print("Guess again.")



game()



