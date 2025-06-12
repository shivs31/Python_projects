#Treasure Island

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?\n")
go = input("Type 'left' or 'right' \n ").lower()

if go== "right":
    print("Game Over.")
elif go == 'left':
    print('You have come to lake.\n There is an island in the middle of the lake.\n')
    next = input("swim or wait \n").lower()
    if next == 'swim':
        print('You got attacked by an angry trout\n')
        print("Game Over.")
    elif next == 'wait':
        last = input('You have arrived island unharmed. There is house with 3 doors. Which door color do you choose? red, blue or yellow\n').lower()
        if last == 'red':
            print("Game Over.")
        elif last == 'blue':
            print("Game Over.")
        else:
            print('You Win!')  
else:
    print('You fell into a hole. Game Over.')

