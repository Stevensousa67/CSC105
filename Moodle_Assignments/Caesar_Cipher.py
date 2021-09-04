# Design and write a Python program that will allow the user to encode and decode messages using this cipher.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# Websites referenced: http://www.asciitable.com/, https://likegeeks.com/python-caesar-cipher/
# Steven Sousa - 11/07/2020


def caesar_encryption(string, shift_number):
    """This function will encrypt a string using Caesar Cipher"""
    ciphered = ""  # Create empty string that will store the ciphered string

    for index in range(len(string)):  # for loop to go over each character of the string
        character = string[index]  # character variable will store each character of the string

        # Check for upper case letters in string
        if character.isupper():

            ciphered += chr((ord(character) + shift_number - 65) % 26 + 65)
        else:
            ciphered += chr((ord(character) + shift_number - 97) % 26 + 97)

    print("Ciphered string: ", ciphered)
    caesar_decryption(ciphered, shift_number)
    return


def caesar_decryption(string, shift_number):
    """This function will decrypt a Caesar ciphered text."""
    decrypted = ""

    for index in range(len(string)):
        character = string[index]

        # Check for upper case letters in string
        if character.isupper():
            decrypted += chr((ord(character) - shift_number - 65) % 26 + 65)
        else:
            decrypted += chr((ord(character) - shift_number - 97) % 26 + 97)

    print("Decrypted string: ", decrypted)
    return


print("This program is an encoder and decoder of Julius Caesar Cipher.")  # Program introduces itself to user
print()

shift_number = int(input("How many shifts would you like to use? The shift can be negative or positive. "))
string = str(input("What is the word? "))  # Ask user for the word
print()

caesar_encryption(string, shift_number)  # Call function
