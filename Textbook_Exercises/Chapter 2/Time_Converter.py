hours_ahead = int(input("How many hours ahead? "))
current_hour = int(input("Choose a time from 0 to 12: "))
final_hour = current_hour + hours_ahead
if final_hour > 24:
    final_hour = (final_hour % 24)
print("It'll be", final_hour, "h")
