#Tip Calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? "))

tip = int(input("How much tip would like to give? 10,12 or 15? "))

people = int(input("How many people to split the bill? "))

each_person_bill = ((total_bill * tip/100) + total_bill) / people

person_pay = round(each_person_bill,2)
print(f"Each person should pay: ${person_pay}")