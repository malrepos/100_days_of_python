import string
import random

print("Welcome the the Password Generator.")

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '?', '/', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

num_letters = int(input("How many letters would you like in your password? "))

num_symbols = int(input("How many symbols would you like? "))

num_numbers = int(input("How many numbers? "))

password_list = []

for element in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for element in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

for element in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(password)
