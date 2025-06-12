# Rock, Scissors and Paper game

# Rock beats Scissors
# Paper beats Rock
# Scissors beat Paper
# Same type draw

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
computer_choice = random.randint(0,2)
print(f'Computer choose : {computer_choice}')

if user_choice >= 3 or user_choice < 0: 
    print("You entered a invalid number. You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!") 
elif user_choice > computer_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")

 