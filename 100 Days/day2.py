#******** Day 2 of 100 days of coding *******
# arithmetic operations
# Tip Calculator

print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
No_people = int(input("How many people to split the bill? "))
pay_amount = (total_bill + tip ) / No_people
print(f"Each person should pay: ${pay_amount}")