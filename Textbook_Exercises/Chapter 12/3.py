# Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical
# listing of all the words, and the number of times each occurs.
# Steven Sousa - Exercise 3 - 12/2/2020

file = open("Alice_Words.txt", "r")
count = {}

for line in file:
    for word in line.split():
        word = word.lower()         # Make every word lower case

        # Remove punctuation to have only words
        word = word.replace('_', '').replace('!', '').replace('.', '').replace('?', '').replace('-', '')
        word = word.replace('(', '').replace(')', '').replace(';', '').replace('"', '').replace(',', '')
        word = word.replace(':', '').replace('[', '').replace(']', '').replace("'", '').replace('...', '')

        # Remove numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()                 # Create keys for dictionary
keys = sorted(keys)                 # Sort keys alphabetically
wordcount = open("Word_Count.txt", "w")     # Create new text file for word count

for word in keys:                   # Iterate over each key
    wordcount.write(word + " " + str(count[word]))      # Write to file the word and how many times it occurs
    wordcount.write('\n')                               # Add \n to end of line

print("Alice appears ", count['alice'], "times.")       # Print how many times alice appears.
file.close()
wordcount.close()