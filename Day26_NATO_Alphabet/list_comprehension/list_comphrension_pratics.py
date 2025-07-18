number = [2,4,6,8]

new_number = [num+2 for num in number]

print(new_number)

#List comprehension for string
name ="Shivani"

letters = [letter for letter in name]
print(letters)

double_num = [num*2 for num in range(1,5)]
[print(double_num)]

#Capital letter
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_list = [name.upper() for name in names if len(name) > 5]

print(new_list)

