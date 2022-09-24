#Christopher Kulpa, Kathleen Clark, Eli (Amy) Geist, Elijah Istchenko
#Group Project 2, creating module
#Module for Temperature conversions
#CSC Python I, Breski
#Fall Semester, 2020

#defining function to turn celcius into fahrenheit
def celsius():
    cTemp1 = float(input("Enter temperature in Celsius: ")) #user input temp in degrees C
    fTemp1 = 9/5 * cTemp1 +32 #convert C to F
    rTemp1 = round(fTemp1, 2) #rounds to 2 decimal places
    print(cTemp1, "Celsius is ", rTemp1, " Fahrenheit") #print result

#defining function to turn fahrenheit into celcius
def fahrenheit():
    fTemp2 = float(input("Enter temperature in Fahrenheit: ")) #user input temp in degrees F
    cTemp2 = (fTemp2 - 32) * 5/9 #convert F to C
    cTemp2 = round(cTemp2, 2)    #rounds to 2 decimal places
    print(fTemp2, "Fahrenheit is ", cTemp2, " Celsius")  #print result

#convert either celcius or fahrenheit to kelvin
def kelvin():
    kDecision = input("Farenheit or Celsius, f/c? Lowercase f or c, please. ") #decide F or C
    if kDecision == "f": #if user picks Fahrenheit, converts to Kelvin like before and prints
        fTemp3 = float(input("Enter temperature in Fahrenheit: ")) # user input F degrees
        kTemp = (fTemp3 - 32) * 5/9 + 273.15 #equation for F to K
        rTemp3 = round(kTemp, 2) #round to 2 decimal places
        print(fTemp3, "Fahrenheit is ", rTemp3, "Kelvin") #print

    if kDecision == "c": #if user picks Celsius, converts to Kelvin and prints
        cTemp3 = float(input("Enter temperature in Celsius: ")) #user input C degrees
        kTemp = cTemp3 + 273.15 #conversion for C to K
        rTemp3 = round(kTemp, 2) #rounding to 2 decimal places
        print(cTemp3, "Celcius is ", rTemp3, "Kelvin") #print


