# Avg_Grade_Fixed
# This program calculates the average of 4 grades based on user input.
# Steven Sousa / Python 1 / 4Cs / 09-13-2020

# Program introduces itself to the user
print("This program will calculate the average of four grades based on your input")
print()

# num will be the counter of grades to be used for the average later.
# it has to start at 0 so that there will be the right amount of numbers to divide.
num = 0

# grade1-4 are the variables where the user will give the grade of each course
grade1 = int(input("Enter first grade: "))

# the use of += makes the counter go up by 1 everytime a grade is given
num += 1
grade2 = int(input("Enter second grade: "))
num += 1
grade3 = int(input("Enter third grade: "))
num += 1
grade4 = int(input("Enter fourth grade: "))
num += 1

# tot is the variable where the sum of all four grades will be allocated
tot = (grade1 + grade2 + grade3 + grade4)

# prints the average (tot/num)
print(f"The average of grades is: {tot/num}")

# Program ends and notifies user
print()
print("Goodbye!")

# Inputs used
# First run: 90, 80, 70, 60 / Average: 75.0
# Second run: 45, 60, 20, 80 / Average: 51.25
# Third run: 10, 0, 40, 70 / Average: 30.0
