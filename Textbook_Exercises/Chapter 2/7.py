print("Compound interest calculator!")
p = 10000
n = 12
r = .08
t = int(input("How many years? "))
z = r/n

a = 10000*(1 + z)**(n*t)
a = round(a, 2)
print(a)
print("Goodbye!")
