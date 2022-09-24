print("This program calculates the amount of gallons of fuel used based on mileage")
print()

miles = int(input("How many miles did you drive? "))
gallons = int(input("How many gallons did you burn? "))
mpg = miles/gallons
mpg = round(mpg, 2)

print("Your MPG was: ", mpg)
print("Goodbye!")
