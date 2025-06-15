import random
stages = ['''
 +---+
 |   |
 0   |               
/|\  |
/ \  |
     |
========
''','''
 +---+
 |   |
 0   |               
/|\  |
/    |
     |
========
''', '''
 +---+
 |   |
 0   |               
/|\  |
     |
     |
========
''', '''
 +---+
 |   |
 0   |               
/|   |
     |
     |
========
''', '''
 +---+
 |   |
 0   |               
 |   |
     |
     |
========
''', '''
 +---+
 |   |
 0   |               
     |
     |
     |
========
''', '''
 +---+
 |   |
     |               
     |
     |
     |
========
'''                         
]
word_list = ["aardvark", "baboon", "camel"]

# create lives to keep track of number of lives left

lives = 6
#Randomly choose a work from the word_list

chosen_word = random.choice(word_list)
print(chosen_word)

#create a no. of blanks as the chosen_word

placeholder = "" 
len_chosen_word = len(chosen_word)

for position in range(len_chosen_word):
    placeholder += "_"
print(placeholder)

# while loop to let the user guess again

game_over = False
correct_letters = []

while not game_over:
    
    #Ask user to guess a letter and make it lower case
    guess = input("Guess a letter from word: ").lower()

    # put the guess letter in right position
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    #to track lives 
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loose")


    if "_" not in display:
        game_over = True
        print("You Win!")
    
    #print the ASCII art from stages to tell user the num of lives remaining

    print(stages[lives])