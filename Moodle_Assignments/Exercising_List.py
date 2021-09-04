# gadgets = [“Cell”, “Laptop”, 100, “Camera”, 310.28, “Ear Buds”, 27.00,
# “Television”, 1000, “Laptop Case”, “Camera Lens”]
# a)Separate strings and numbers into their own lists.
# b)Sort and display the strings list in ascending order
# c)Sort and display the strings list into a new list in descending order
# d)Sort the number list from lowest to highest
# e)Find the highest number in the list
# Steven Sousa - Exercising a List - 11/17/2020

gadgets = ["Cell", "Laptop", 100, "Camera", 310.28, "Ear Buds", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

# A) Separate strings and numbers into their own lists.
number_list = [x for x in gadgets if isinstance(x, int)]      # Place only integers in number_list from gadgets
decimal_list = [x for x in gadgets if isinstance(x, float)]   # Place only floats in float_list from gadgets
string_list = [x for x in gadgets if isinstance(x, str)]      # Place only strings in string_list from gadgets
number_list = number_list + decimal_list                      # Concatenate number list with float list

print("Numerical List:", number_list)
print("String List:", string_list)

# B) Sort and display the strings list in ascending order
string_list.sort()                                          # Sort string_list in alphabetical order
print("Sorted in ascending order:", string_list)

# C) Sort and display the strings list into a new list in descending order
second_string_list = string_list                            # Copy string_list into a new second_string_list
second_string_list.sort(reverse=True)                       # Sort second_string_list in reversed order
print("Second string list in reverse:", second_string_list)

# D) Sort the number list from lowest to highest
number_list.sort()                                          # Sort number_list in ascending order
print("Sorted number list:", number_list)

# E) Find the highest number in the list
number_list.sort()                            # Sort number_list in ascending order so that largest number is at the end
print("Largest number:", number_list[-1])     # Print only the last element from number_list (which is the largest)
