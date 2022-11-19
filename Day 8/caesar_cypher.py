# create a list of the letters of the alphabet
# do it twice to solve the index out of range issue
alphabet = []

for i in range(97, 123):
    alphabet.append(chr(i))
for i in range(97, 123):
    alphabet.append(chr(i))


# def encrypt(plain_text, shape_shift):
#     encrypted_message = ""
#     for letter in plain_text:
#         letter_index = alphabet.index(letter)

#         new_letter = (alphabet[letter_index+shape_shift])
#         encrypted_message += new_letter
#     print(f"The encode text is {encrypted_message}.")


# def decrypt(encrypted_message, shape_shift):
#     decrypted_message = ""
#     for letter in encrypted_message:
#         letter_index = alphabet.index(letter)

#         new_letter = (alphabet[letter_index-shape_shift])
#         decrypted_message += new_letter
#     print(f"The decrypted message is {decrypted_message}.")

# ask the user for inputs

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

# the function taking the inputs


shift = shift % 26


def caesar(_text, _shift, _direction):
    encrypted_message = ""
    decrypted_message = ""
    if _direction == "encode":
        for letter in _text:
            if letter not in alphabet:
                encrypted_message += letter
                continue
            letter_index = alphabet.index(letter)

            new_letter = (alphabet[letter_index+_shift])
            encrypted_message += new_letter
        print(f"The encoded text is {encrypted_message}.")
    elif _direction == "decode":
        for letter in _text:
            if letter not in alphabet:
                decrypted_message += letter
                continue
            letter_index = alphabet.index(letter)

            new_letter = (alphabet[letter_index-_shift])
            decrypted_message += new_letter
        print(f"The decrypted message is {decrypted_message}.")
    choice = input(
        "Type 'yes' if you want to go again, otherwise type 'no':\n").lower()
    if choice == 'yes':
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("Goodbye.")


# call the function with user inputs
caesar(text, shift, direction)
