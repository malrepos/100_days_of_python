from tkinter import Y


age = int(input("Please enter your age: "))

years_left = 90 - age

days = years_left*365
weeks = years_left*52
months = years_left*12

print(
    f"You have {days} days, {weeks} weeks, and {months} months left to live.")
