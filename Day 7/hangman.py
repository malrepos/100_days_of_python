import random
import hangman_ascii

print(hangman_ascii.opening)

# get the words from the file
# split into words
word_list = hangman_ascii.word_list.split()

# choose a word from the word list randomly
word_choice = random.choice(word_list)

# a print satement for word choice for testing
print(f"The hidden word is {word_choice}")

# an empty list to display the spaces remaining in the word
display = []

# fill the display list with spaces for number of letters
for letter in word_choice:
    display.append("_")
print(display)

# the hangmanpics is in order so I reversed the lives number
lives = -(len(hangman_ascii.HANGMANPICS))
game_on = True
while game_on == True:
    guess = input("Guess a letter: ").lower()

    i = 0

# if the user gets the guess wrong
# lives is added taking the lives closer to the end of the game
    if guess not in word_choice or guess == "":
        lives += 1
        print(lives)

# if letter is is in the word:
# the letter in the word is shown
# the pic for lives left is displayed
    for letter in word_choice:
        if guess == letter:
            display[i] = letter
        i += 1
    print(hangman_ascii.HANGMANPICS[lives])
    print(display)

# if there are no more "_" in the word ie. no more empty spaces:
# the player wins
# the while loop is released
    if "_" not in display:
        game_one = False
        print("You win!")
        break
# if there are no more lives left
# the player loses
# break out of the while loop
    elif lives == -1:
        print("You lose!")
        game_on = False
        break
    else:
        continue
