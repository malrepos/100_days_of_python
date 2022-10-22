print("Welcome to the Love Machine!")

name1 = input("What is your name?\n").lower()
name2 = input("What is the name of your crush? \n").lower()

combine_name = name1 + name2


test = "true love"
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

true = str(t+r+u+e)
love = str(l+o+v+e)

love_score = int(true+love)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}. You go together like coke and mentos.")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score}. You are okay together. Nothing great.")
else:
    print(f"Your love score is {love_score}.")
