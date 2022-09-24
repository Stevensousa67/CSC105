# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for
# each student, and print out the student’s name along with their average grade.
# Steven Sousa - Exercise 2 - 11/26/2020

file = open("studentdata.txt", "r")             # Open studentdata.txt for reading

for line in file:                               # Iterate over each line of the file
    total = 0                                   # Set total to 0 for sum of grades
    index = line.split()                        # Convert line into a list
    new_list = index[1:]                        # Create new list using only the grades

    for i in range(len(new_list)):              # Iterate over each index of list
        new_list[i] = int(new_list[i])          # Convert each index from list into int

    average = sum(new_list)/len(new_list)       # Sum new_list values and divide by amount of values
    average = round(average, 2)                 # Round average to 2 decimals
    print(index[0], "average grade: ", average)

file.close()
