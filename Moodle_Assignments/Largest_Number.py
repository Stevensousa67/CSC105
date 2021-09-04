# This code will print the largest number within a list
# Steven Sousa / 4Cs / Python 10-15-2020

x = int(input("What will be the value of x? "))
y = int(input("What will be the value of y? "))
z = int(input("What will be the value of z? "))

if z > y and z > x:
    print(z)
elif x > y and x > z:
    print(x)
elif y > z and y > z:
    print(y)

print()
print("Goodbye")
