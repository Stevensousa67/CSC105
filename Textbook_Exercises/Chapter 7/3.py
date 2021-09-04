# Write a function that returns a grade letter in string format according to the mark received.
# Steven Sousa - Exercise 3 - 10/20/2020

# Define variables
mark = 0


def getGrade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


mark = float(input("Choose a mark between 0 and 100: "))
print("Mark:", mark, "Grade:", getGrade(mark))

print()
print("Goodbye")

# Tests performed: 89, 89.999, and 90
