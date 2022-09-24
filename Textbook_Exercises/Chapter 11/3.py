# Using the text file studentdata.txt write a program that calculates the minimum and maximum score for each student.
# Print out their name as well.
# Steven Sousa - Exercise 3 - 11/26/2020

file = open("studentdata.txt", "r")             # Open studentdata.txt

for line in file:                               # Iterate over each line in file
    index = line.split()                        # Convert line into a list

    for i in range(len(index[1:])):              # Iterate over each index starting at 1
        index[i+1] = int(index[i+1])             # Convert each index into integer

    # Use max() and min() function on list to find highest and lowest values
    print(index[0], "Highest grade is", max(index[1:]), "and lowest grade is", min(index[1:]))
file.close()
