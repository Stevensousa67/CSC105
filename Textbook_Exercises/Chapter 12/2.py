# Be sure you understand why you get each result. Then apply what you have learned to fill in the body of the
# function below, and add code for the tests indicated:
# def add_fruit(inventory, fruit, quantity=0):
#      pass
# make these tests work...
# new_inventory = {}
# add_fruit(new_inventory, 'strawberries', 10)
# #  test that 'strawberries' in new_inventory
# #  test that new_inventory['strawberries'] is 10
# add_fruit(new_inventory, 'strawberries', 25)
# test that new_inventory['strawberries'] is now 35)
# Steven Sousa - Exercise 2 - 12/02/2020

def add_fruit(inventory, fruit, quantity):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory


new_inventory = {}

add_fruit(new_inventory, 'strawberries', 10)
print("First test:", new_inventory)

add_fruit(new_inventory, 'strawberries', 25)
print("Second test:", new_inventory)
