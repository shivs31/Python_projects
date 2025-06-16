def calculate_love_score(name1, name2):
  combined_names = (name1 + name2).lower()

  true_count = 0
  for letter in "true":
    true_count += combined_names.count(letter)

  love_count = 0
  for letter in "love":
    love_count += combined_names.count(letter)

  love_score = int(str(true_count) + str(love_count))
  print(love_score)

# Call your function with hard coded values
calculate_love_score("Shivani", "Keerthi")