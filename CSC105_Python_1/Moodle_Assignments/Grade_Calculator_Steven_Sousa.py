# This code will calculate the grade average of any given number of grades, and convert the numerical grade to
# a letter grade. Finally, at the end of the code, I wrote a description of how I would reverse-engineer
# this code to convert from letter form to number form.
# Steven Sousa / Python / 4Cs / 10-15-2020

# Declare variables
total = 0


# Create function that will transform the grade average into letter grade
# I chose not to return anything because the program ends after it converts numeric grade to letter grade.
def letter_grade_func(average):
    """Receive the average numeric grade to be converted to letter grade."""
    if average >= 93:
        print("Congrats! That's an A")
    elif average >= 90:
        print("That's an A-")
    elif average >= 87:
        print("That's a B+")
    elif average >= 83:
        print("That's a B")
    elif average >= 80:
        print("That's a B-")
    elif average >= 77:
        print("That's a C+")
    elif average >= 73:
        print("That's a C")
    elif average >= 70:
        print("That's a C-")
    elif average >= 67:
        print("That's a D+")
    elif average >= 63:
        print("That's a D")
    elif average >= 60:
        print("That's a D-")
    else:
        print("Sorry, but you Failed...")


# Program introduces itself to user
print("This program will convert a number grade average to letter grade. ")

# Ask user how many grades will be averaged
number_of_grades = int(input("How many grades do you want averaged? "))

# Create for statement to add up grades
for a in range(number_of_grades):
    score = float(input("What is the score of this grade? "))
    total = total + score

# Calculate average
average = total / number_of_grades
print("The grade average is: ", average)

# Send average to function
letter_grade_func(average)

#  Describe how you might take letter grades as input and report the average as a numeric grade.

# I would modify my program to send a letter grade to "letter_grade_func(average)" function,
# and change the conditional statements to say that if the average is a certain letter,
# then the numeric grade will be in between the range of numbers that constitute the letter grade.
# Ex: if the letter average is A, then the numeric grade will be between 93 and 100.
