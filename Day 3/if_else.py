print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    photo = input("Do you want a photo? y or n: ")
    if age < 12:
        total_bill += 5

    elif age >= 12 and age < 18:
        total_bill += 7

    elif age >= 45 and age <= 55:
        total_bill = 0
    else:
        total_bill += 12

    if photo == "y":
        total_bill += 3

    print(f"The total bill is ${total_bill}")

else:
    print("Bad luck short arse!")
