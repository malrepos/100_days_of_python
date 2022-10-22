import random
# import ascii art
import rock_paper_scissors as rps

# set a list of possible choices
hand = [0, 1, 2]
# make a choice randomly for the computer
computer_choice = random.choice(hand)

# get the users choice and convert to integer
choice = int(input(
    "What is your choice? Choose 0 for Rock, choose 1 for Paper, choose 2 for Scissors: "))
if choice >= 3:
    print("You didn't choose 0, 1 or 2 did you? You lose.")
else:
    # print the ascii art of the users choice
    print(f"You chose {rps.art[choice]}")
    # print the ascii art of the computer's choice
    print(f"Computer chose {rps.art[computer_choice]}")

    # set the conditions for win, lose or draw
    if choice == 0 and computer_choice == 1:
        print("You lose")
    elif choice == 0 and computer_choice == 2:
        print("You win")
    elif choice == 0 and computer_choice == 0:
        print("It's a draw")
    elif choice == 1 and computer_choice == 0:
        print("You win")
    elif choice == 1 and computer_choice == 1:
        print("It's a draw")
    elif choice == 1 and computer_choice == 2:
        print("You lose")
    elif choice == 2 and computer_choice == 0:
        print("You lose")
    elif choice == 2 and computer_choice == 1:
        print("You win")
    elif choice == 2 and computer_choice == 2:
        print("It's a draw")
