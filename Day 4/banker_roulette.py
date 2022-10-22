import random

names_string = input("Give me everybody's names, separated by a comma: ")

# split the names_string into a list of names
names = names_string.split(", ")

# generate a random integer between 0 and the length of names list
# -1 for index range of list
choice = random.randint(0, (len(names)-1))

print(names[choice])
