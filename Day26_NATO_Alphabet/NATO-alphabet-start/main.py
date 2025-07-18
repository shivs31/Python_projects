# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# students_score ={student:score for (student, score) in zip(student_dict['student'], student_dict['score'])}
# print(students_score)

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# student_score = {row.student : row.score for (index, row) in student_data_frame.iterrows() if row.student == 'Angela'}
# print(student_score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv('/Users/shivani/udemy_ds/python_projects/Day26_NATO_Alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)