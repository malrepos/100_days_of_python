print("Welcome to the Tip Calculator.")

total_bill = float(input("What ws the total bill? $"))

tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

num_of_people = int(input("How many people to split the bill? "))

tip = (total_bill * (tip_percentage/100))
bill_per_person = ((total_bill + tip) / num_of_people)
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}.")
