# This program calculates a workers gross and net paycheck, based on a $17.50/h
# Steven Sousa / Python1 / 4Cs

# Program introduces itself to the user
print("Welcome to the paycheck calculator. The compensation is $17.50/h.")

# Program asks for amount of hours and calculates the gross pay
# x is the variable that'll multiply hours times wage
hours = input("How many hours did the employee work? ")
hours = float(hours)
x = (hours*17.50)
print()
print(f"Gross income: ${x}")
print()

# Program calculates and prints each taxes
# st is State Tax / ft is Federal Tax / SS is Social Security
st = (x*.05)
print(f"State tax: ${st}")

ft = (x*.10)
print(f"Federal tax: ${ft}")

ss = (x*.075)
print(f"Social Security tax: ${ss}")

# Program prints total amount of taxes withheld
# y is the variable that adds up all the 3 types of taxes
y = (st+ft+ss)
print(f"Total taxes: ${y}")
print()

# Program prints net pay
print(f"Net pay: ${x-y}")

# Program ends
print()
print("Good bye.")
