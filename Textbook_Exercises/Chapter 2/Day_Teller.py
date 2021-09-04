print("Tip: Sunday = 0 and Saturday = 6.")
print()

current_day = int(input("What day of the week is it? "))
days_ahead = int(input("How many days will you be out? "))
future_day = (current_day + days_ahead)

if future_day > 6:
    future_day = future_day % 7
if future_day == 0:
    print("It'll be a Sunday.")
if future_day == 1:
    print("It'll be a Monday.")
if future_day == 2:
    print("It'll be a Tuesday.")
if future_day == 3:
    print("It'll be a Wednesday.")
if future_day == 4:
    print("It'll be a Thursday.")
if future_day == 5:
    print("It'll be a Friday.")
if future_day == 6:
    print("It'll be a Saturday.")
