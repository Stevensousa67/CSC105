# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a
# poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then
# keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:
# Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.

def char_count(text):
    """ This function will count how many alphabetic characters in a text"""
    total_char = 0
    total_e = 0

    for total in text:
        # Check for spaces so that total count doesn't increase
        if total == " ":
            total_char = total_char
        # Check for ,!?.- ... so that total count doesn't increase
        elif total == ',' or total == '!' or total == '?' or total == '.' or total == '...' or total == '-'\
                or total == '/' or total == '_' or total == '(' or total == ')' or total == '$':
            total_char = total_char
        # Check for e so that total_e character and total_char can increase
        elif total == 'e':
            total_e += 1
            total_char += 1
        # Let total_char increase with any other characters
        else:
            total_char += 1

    # Get percentage of text that is made up of 'e'
    percentage = (total_e / total_char) * 100

    # print different statements according to total 'e' count.
    if total_e > 1:
        # If total_e count is above 1, print the following statement:
        print("Your text contains", total_char, "alphabetical characters, of which", total_e, "(", percentage,"%) are "
                                                                                                              "'e'.")
        # If total_e count is 1, print the following statement:
    elif total_e == 1:
        print("Your text contains", total_char, "alphabetical characters, of which", total_e, "(", percentage,"%) is "
                                                                                                              "'e'.")
    else:
        # If total_e count is 0, print the following statement:
        print("Your text contains", total_char, "alphabetical characters, of which none (", percentage, "%) is an 'e'.")


string = str(input("What is the text? "))
char_count(string)

