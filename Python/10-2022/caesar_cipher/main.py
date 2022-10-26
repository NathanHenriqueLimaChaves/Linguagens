"""Creating an Caesar Cipher!"""

import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    if (direction == 'encode'):
        for char in start_text:
            if char in alphabet:
                index = alphabet.index(char)
                final_index = index + shift
                if (final_index > 25):
                    final_index = final_index % 25
                    final_char = alphabet[final_index]
                    end_text.append(final_char)
                else:
                    final_char = alphabet[final_index]
                    end_text.append(final_char)
            else:
                end_text.append(char)
        encod_text = str(''.join(end_text))
        print(f"Here`s the encode result: {encod_text}")

    elif (direction == 'decode'):
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                final_index = index - shift
                if (final_index < 0):
                    final_index = final_index * -1
                    alphabet_rervers = list(reversed(alphabet))
                    final_char = alphabet_rervers[final_index]
                    end_text.append(final_char)
                else:
                    final_char = alphabet[final_index]
                    end_text.append(final_char)
            else:
                end_text.append(char)
        decod_text = str(''.join(end_text))
        print(f"The decoded text is: {decod_text}")

    else:
        os.system("cls")
        print(
            "Sorry, you didn`t choose a valid option. Choose between 'encode' or 'decode', please.\n")


print(logo)

restart = True
while restart == True:
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    restart = input("").lower()
    if (restart == 'no'):
        restart = False
        print("\nGoodbye!\n")
    elif (restart == 'yes'):
        restart = True
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if (shift < 0):
            os.system("cls")
            print("The shift number can`t be negative.\n\n")
            break
        elif (shift > 26):
            shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
