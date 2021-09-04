# Write a recursive function to reverse a list.
# Steven Sousa - Exercise 2 - 10/29/2020

def reverseList(list):
    """This function will reverse a given list."""
    backwards = []
    length = len(list)
    if length == 0:
        return

    backwards = list[length - 1]
    print(backwards, end="")
    reverseList(list[0:length-1])


list = []
quantity = int(input("How many words or numbers inside the list? "))

for a in range(quantity):
    list.append(input("Enter a name or value: "))

print("Original list: ", list)
#print("Length is: ", len(list))
reverseList(list)


