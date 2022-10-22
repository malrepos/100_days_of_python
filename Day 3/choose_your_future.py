print('''
   ,    ,    /\   /\
  /( /\ )\  _\ \_/ /_
  |\_||_/| < \_   _/ >
  \______/  \|0   0|/
    _\/_   _(_  ^  _)_
   ( () ) /`\|V"""V|/`\
     {}   \  \_____/  /
     ()   /\   )=(   /\
     {}  /  \_/\=/\_/  \
''')

print("Welcome to 'The Hunt for the End'")
print("Your mission is to find the end and exit the game.")

print("You are 40 years old.\nYou are t a crossroad in you life.")
print("Where do you want to go? You can try to go up. Or easily go down.")
choice1 = input("Type 'up' or 'down'\n").lower()

if choice1 == 'up':
    print("You now have to work your arse off. Fair enough.")
    print("But what will you work on?")
    print("You have two choices: work on your career, or work on your personality.")
    choice_2a = input(
        "To work on your career, type 'career'. To work on your image, type 'personality': \n").lower()
    if choice_2a == 'career':
        print("Now you gotta work. And really, what you have to do is sacrifice.")
        print("This will take a long time. Maybe years.")
        print("They key to success? Habits. Build good habits.")
    elif choice_2a == 'personality':
        print("What does 'personality' even mean!?")
        print("I think what it comes down to is you and other people.")
        print("Relationships.")
        print("Congratulations. You have a lot of friends and people seem to like you.")
        print("Are you happy. Probably.")


elif choice1 == 'down':
    print("You still have to work, but you will have a lot of free time.")
    print("What will you do with it?")
    choice_2b = input(
        "To play computer games, type 'games'. To take drugs, type 'drugs': \n").lower()
    if choice_2b == 'games':
        print("Congratulations1 You have distracted yourself. You have also gotten some enjoyment out of your choice. You made some shallow friends. But now you are old and have very little. You do have some decent memories though.")
    elif choice_2b == 'drugs':
        print("It started out pretty well. But things got pretty pathetic pretty quick. You are dependent. Your mind is slow and dull. You have very little motivation to do anything. You distracted yourself. Now, despite losing most of your mind, there is still enough of you there to know you screwed up.")
