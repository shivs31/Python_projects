# student_scores = [3,4,10,5,5]
# # highest_score = max(student_scores)
# # print(highest_score)

# max = 0
# for score in student_scores:
#     if score > max:
#         max = score
# print(max)

#Gauss Challenge

# sum = 0
# for n in range(1,101):
#     sum += n
# print(sum)

## PyPassword Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*']

l = int(input("How many letters would you like to have?\n"))
n = int(input("How many numbers you would like to have?\n"))
s = int(input("How many symbols you would like to have?\n"))

#List because to generate password randomly
password_list = []

for char in range(0, l):
    password_list.append(random.choice(letters))

for char in range(0,n):
    password_list.append(random.choice(numbers))

for char in range(0,s):
    password_list.append(random.choice(symbols))

print(password_list)

#function to  strengthened password
random.shuffle(password_list)
print(password_list)

# to convert the list into string password
password = ""
for char in password_list:
    password += char    
print(f"Your password is : {password}")