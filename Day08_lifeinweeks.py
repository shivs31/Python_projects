def life_in_weeks(age):
  weeks_in_a_year = 52
  max_age = 90
  total_weeks = max_age * weeks_in_a_year
  weeks_lived = age * weeks_in_a_year
  weeks_left = total_weeks - weeks_lived
  print(f"You have {weeks_left} weeks left.")

# Call your function with a hardcoded value
life_in_weeks(56)