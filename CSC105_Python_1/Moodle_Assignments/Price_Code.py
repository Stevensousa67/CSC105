# This is the main program that will give the final price on a given item price
# Creators: Steven Sousa, Gabriele Narmontaite, Liam Benway, Patrick Leddy
# 4Cs / Python / 10-6-2020

# Import the Tax_Calculator module
import Tax_Calculator

# Define variables
price = 0

# Ask user for the price of a item
price = float(input("What is the price of the item? "))

# Ask user which state he resides in
state = str(input("Choose the state: MA, RI, or NH "))

# Create condition where the program sends the right info based on the state selected

if state == "MA" or state == "ma" or state == "massachusetts" or state == "Massachusetts":
    Tax_Calculator.ma_state_tax(price)
    ma_answer = f'The total price is: ${Tax_Calculator.ma_state_tax(price)}'
    print(ma_answer)


elif state == "RI" or state == "ri" or state == "Rhode Island" or state == "rhode island":
    Tax_Calculator.ri_state_tax(price)
    ri_answer = f'The total price is: ${Tax_Calculator.ri_state_tax(price)}'
    print(ri_answer)


elif state == "NH" or state == "nh" or state == "New Hampshire" or state == "new hampshire":
    Tax_Calculator.nh_state_tax(price)
    nh_answer = f'The total price is: ${Tax_Calculator.nh_state_tax(price)}'
    print(nh_answer)

else:
    print("Invalid entry. Please try again.")
