PLACEHOLDER = "[name]"

with open("/Users/shivani/udemy_ds/python_projects/Day24_Mail_Merge_Project_Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() #readlines converts each line in a file into a list
    print(names)


with open("/Users/shivani/udemy_ds/python_projects/Day24_Mail_Merge_Project_Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    #for each name in invited_names.txt
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #Save the letters in the folder "ReadyToSend".
        with open(f"/Users/shivani/udemy_ds/python_projects/Day24_Mail_Merge_Project_Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode ="w") as completed_letter:
            completed_letter.write(new_letter)





    