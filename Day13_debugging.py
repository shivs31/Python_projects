#debugging practice

#range high value is not included
def my_function():
    for i in range(1,20): #add 21 instead of 20 
        if i == 20:
            print("you got it")

my_function()

#Reproduce the Bug
#List index starts with 0 and randint high value 6 is out of range
from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1,6) #fix code to randint(0,5)
print(dice_images[dice_num])

#3. computer play debug

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Try and Except for Red Underline errors

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print("You can drive at age {age}.") #This should a f string
