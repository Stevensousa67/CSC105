# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter occurs.
# Case should be ignored. A sample run of the program might look this this:
# Please enter a sentence: ThiS is String with Upper and lower case Letters.
# a  2
# c  1
# d  1
# e  5
# g  1
# h  2
# i  4
# l  2
# n  2
# o  1
# p  2
# r  4
# s  5
# t  5
# u  1
# w  2
# Steven Sousa - Exercise 1 - 11/29/2020

string = str(input("Enter a string: "))         # Get string from user
string = string.lower()                         # Make any upcase letters lowercase
alphabet = 'abcdefghijklmnopqrstuvwxyz'         # Create alphabet for comparison
character_count = {}                            # Create empty dictionary

for character in string:                        # Iterate over each character of string
    if character in alphabet:                   # Check if character is in alphabet
        if character in character_count:        # Check if character is in dictionary
            character_count[character] = character_count[character] + 1     # Add letter count to dictionary
        else:
            character_count[character] = 1

keys = character_count.keys()                   # Show only the keys in dictionary
for character in sorted(keys):                  # Iterate over each letter of dictionary alphabetically
    print(character, character_count[character])
