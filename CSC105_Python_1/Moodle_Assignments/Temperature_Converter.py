# This program converts temperature from Celsius to Fahrenheit or vice-versa.
# Steven Sousa / Computer Science / 4Cs / Python 1

# Declare variable
z = float()
end = str()

# The program introduces itself to the user
print('This program converts temperature units from Celsius to Fahrenheit or vice-versa based on the unit you choose. '
      'Type exit when you are done')

# Create an infinite loop so that the program will request a valid input instead of stopping otherwise
while True:

    # Ask user what unit is going to be converted
    Unit = input('Select C or F: ')

    # Create condition that if user types exit, the program will end (break the loop) 
    if Unit == "exit" or Unit == "Exit":
        end = str(Unit)
        break

    # Create condition that if user selects F or Fahrenheit, the program will execute code below:
    if Unit == "F" or Unit == "Fahrenheit" or Unit == "f" or Unit == "fahrenheit":

        # If user input is correct, then the program will continue
        x = input("Great! What is the temperature in Fahrenheit? ")
        x = float(x)
        z = (x - 32) / 1.8
        z = round(z, 1)
        print(f'In Celsius, that would be: {z}')

    # Create condition that if user selects C or Celsius, the program will execute code below:
    elif Unit == "C" or Unit == "Celsius" or Unit == "c" or Unit == "celsius":

        # If user input is correct, then the program will continue
        x = input("Great! What is the temperature in Celsius? ")
        x = float(x)
        z = (x * 1.8) + 32
        z = round(z, 1)
        print(f'In Fahrenheit, that would be: {z}')

    # Create condition that if the user doesn't choose either units, to prompt a fail
    elif Unit != "F" or Unit != "Fahrenheit" or Unit != "f" or Unit != "fahrenheit" or \
            Unit != "C" or Unit != "Celsius" or Unit != "c" or Unit != "celsius":

        print("Sorry, that's an invalid entry. ")
