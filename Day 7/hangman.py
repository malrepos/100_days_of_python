import random

word_list = ["ardvark", "baboon", "camel"]

word_choice = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in word_choice:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

print(guess)


print(choice)
