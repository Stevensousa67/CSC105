# What is the longest word in Alice in Wonderland? How many characters does it have?
# Steven Sousa - Exercise 4 - 12/3/2020

file = open("Word_Count.txt", "r")      # Open Word_Count.txt file for reading
largest_word = ""

for line in file:
    index = line.split()
    if len(index[0]) > len(largest_word):
        largest_word = index[0]

print("Largest word in the book is:", largest_word)
file.close()
