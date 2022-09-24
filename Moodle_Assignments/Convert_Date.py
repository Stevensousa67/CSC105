# Program that converts the numerical date into string .
# This program was built referencing prof. David Breski's example, as it portrayed my line of thought during class.
# Steven Sousa - 11/16/2020

def convert_month(month):
    """This function will convert numerical month into string month"""
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"


date = input("Enter a numerical date as mm/dd/yyyy: ")   # Get numerical date from user
date1 = date.split('/')                                  # Create list that holds each value of date separated by /

month = convert_month(int(date1[0]))    # Convert numerical to verbal. Send to function the int of date1 at position 0
print(month + "", int(date1[1]), ", " + date1[2])        # print converted date format.
