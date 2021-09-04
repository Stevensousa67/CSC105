# This program will collect temperature from the user and call Group 1's Module to convert to a different unit
# Creators: Steven Sousa, Gabriele Narmontaite, Patrick Leddy, Liam
# 4Cs / Python / 10-7-2020

# Import Group 1's Module.
import TempConversionModule

# Define variables
temp_unit = 0  # This variable will be used to ask for the initial temperature unit
unit_converted = 0  # This variable will be used to ask for the unit to be converted to

# Ask user what temperature to start with
temp_unit = str(input("What is the starting unit of measure? "))

# If the user chooses Kelvin, the main program will call the .kelvin function from the module right away without
# asking for the unit to be converted to, because the function has a print statement that asks for that already.
# (little work around)
if temp_unit == "K" or temp_unit == "k" or temp_unit == "Kelvin" or temp_unit == "kelvin":
    temp_unit = TempConversionModule.kelvin()   # temp_unit will call the kelvin function.

# Ask user to what unit of measure to convert to
unit_converted = str(input("What will it convert to? "))

# Create a conditional statement to avoid user error. By making all of these "or's" the program can recognize more ways
# of choosing a temperature unit.

# This if statement is for when the user chooses F
if temp_unit == "F" or temp_unit == "f" or temp_unit == "Fahrenheit" or temp_unit == "fahrenheit":
    # This if statement is for when the user chooses to convert from F to C
    if unit_converted == "C" or unit_converted == "c" or unit_converted == "Celsius" or unit_converted == "celsius":
        temp_unit = TempConversionModule.fahrenheit()  # temp_unit will call the fahrenheit function.

    # This elif statement is for when the user chooses to convert from F to K
    elif unit_converted == "K" or unit_converted == "k" or unit_converted == "Kelvin" or unit_converted == "kelvin":
        temp_unit = TempConversionModule.kelvin()  # temp_unit will call the kelvin function

# This elif statement is for when the user chooses C as the starting unit of measure
elif temp_unit == "C" or temp_unit == "c" or temp_unit == "Celsius" or temp_unit == "celsius":
    # This if statement is for when the user chooses to convert from C to F
    if unit_converted == "F" or unit_converted == "f" or unit_converted == "Fahrenheit" \
            or unit_converted == "fahrenheit":
        temp_unit = TempConversionModule.celsius()  # temp_unit will call the celsius function.

    # This elif statement is for when the user chooses to convert from C to K
    elif unit_converted == "K" or unit_converted == "k" or unit_converted == "Kelvin" or unit_converted == "kelvin":
        temp_unit = TempConversionModule.kelvin()  # temp_unit will call the kelvin function.

# Disclaimer 1: Whenever you choose to convert to K, the function will ask you to choose
# the initial unit of measure again. This is because of the way the module was coded
# and no work around could be made to avoid this redundancy without having to change the module.
# Disclaimer 2: We had to change their fahrenheit function in order to make it work as expected.
# No changes to the essence of their train of thought, just renamed the variables to what they should've been using.
