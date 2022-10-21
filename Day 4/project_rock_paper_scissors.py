import random

hand = [0, 1, 2]
computer_choice = random.choice(hand)

choice = input(
    "What is your choice? Choose 0 for Rock\nchoose 1 for Paper\nchoose 2 for Scissors")


print(choice)
print(f"Computer chose {computer_choice}")

if choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 0 and computer_choice == 2:
    print("You win")
elif choice == 0 and computer_choice == 0:
    print("It's a draw")
