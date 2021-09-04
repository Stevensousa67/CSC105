# The following sample file called studentdata.txt contains one line for each student in an imaginary class.
# The student’s name is the first thing on each line, followed by some exam scores.
# The number of scores might be different for each student. Using the text file studentdata.txt write a program that
# prints out the names of students that have more than 6 quiz scores.
# Steven Sousa - Exercise 1 - 11/26/2020


student_list = open("studentdata.txt", "r")     # Read studentdata.txt file

for line in student_list:                       # iterate line by line
    index = line.split()                        # Make each line a list
    if len(index[1:]) > 6:                      # Check to see if a student has more than 6 grades (excludes name)
        print(index[0])                         # Prints the student's name if more than 6 grades

student_list.close()                            # Close the studentdata.txt file

print()
print("Goodbye!")
