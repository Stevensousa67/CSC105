# Pocket_Change_Converter
# This program tells user how much pocket change a person has and converts to Euro
# Steven Sousa / Python1 / 4Cs / 09-13-2020

# Program introduces itself to the user
print("This program will say how much pocket change you have. It'll also convert the amount to euro.")
print()

# Program asks user how many of each coin he has
# p is penny / n is nickel / d is dime / q is quarter
# variables a, b, c, and e store the product of each coin based on user input
p = input("How many pennies do you have? ")
p = float(p)  # using p=float(p) will make the amount of pennies a real number, making it easier to multiply later.
a = float(p*.01)

n = input("How many nickels do you have? ")
n = float(n)
b = (n*.05)

d = input("How many dimes do you have? ")
d = float(d)
c = (d*.1)
c = round(c, 1)  # This will keep dimes to one number after decimal point.
# I was having a glitch where it would have lots o 0s after the decimal point

q = input("How many quarters do you have? ")
q = float(q)
e = (q*.25)

# Program will calculate and display how much change the user has for each type of coin
print()
print("Total in pennies:", a)
print("Total in nickels:", b)
print("Total in dimes:", c)
print("Total in quarters", e)

# Program prints total amount of change rounded to two numbers after decimal point
a = round(a, 2)
b = round(b, 2)
c = round(c, 2)
e = round(e, 2)
print(f"Total amount of change: ${a+b+c+e}")

# Program converts, rounds to two decimal points, and prints total pocket change into Euro
# (Currency is 1 EURO = 1.18 USD)
euro = (a+b+c+e)/1.18
euro = round(euro, 2)
print("In Euro, you would have:", euro)

# Program ends and notifies user
print()
print("Goodbye!")

# Inputs tested
# p = 1; n = 2; d = 3; q = 4 / Total USD: $1.41 / Total Euro: $1.19
# p = 10; n = 4; d = 10; q = 4 / Total USD: $2.30  / Total Euro: $1.95
# p = 5; n = 0; d = 20; q = 12 / Total USD: $5.05  / Total Euro: $4.28
