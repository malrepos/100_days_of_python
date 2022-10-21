import random

names_string = input("Give me everybody's names, separated by a comma: ")

names = names_string.split(", ")

choice = random.randint(0, (len(names)-1))

print(names[choice])
