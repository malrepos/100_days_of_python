import random

word_list = ["ardvark", "baboon", "camel"]

word_choice = random.choice(word_list)

print(word_choice)

display = []

for letter in word_choice:
    display.append("_")
print(display)

guess = input("Guess a letter: ").lower()

i = 0
for letter in word_choice:
    if guess == letter:
        display[i] = letter
    i += 1
print(display)
