# The area of a circle is defined by A= N * R^2, where N is equal to 3.14159 (aka pi)

r = input('What will be the radius of the circle? ')
r = float(r)
pi = 3.14159
a = pi*(r**2)
a = round(a, 2)

print("The area of the circle is:", a)
print("Goodbye!")
