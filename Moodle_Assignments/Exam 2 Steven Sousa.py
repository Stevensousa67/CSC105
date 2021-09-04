# *** Final Thoughts: I ran into a problem that I couldn't find a solution to while having feature creep:
# 1) I couldn't find a way to update the cart price if the customer decided to remove an item from it. I got the cart
# dictionary to update, it is just the total price that I don't know how to update.
# I would really appreciate your feedback as to how to fix these issues, professor. The section where I started having
# feature creep is commented out near the end of the code (where i intended to have them).
# Steven Sousa - Exam II - 12-7-2020

# Create a store with items that are sold and their respective quantity in stock.
store = {'Phones': 10, "Cases": 50, "Headphones": 40, "Laptops": 10, "Mouse": 30, "Cables": 60,
         "Pendrive": 5}

# Create variables that will hold the price of each item in the store
phone_cost = 600
case_cost = 20
headphone_cost = 150
laptop_costs = 1100
mouse_cost = 70
cables_cost = 10
pendrive_cost = 30

while True:

    # Create an empty shopping cart to be filled by user and empty price list
    shopping_cart = {}
    price_list = []
    quantity = 0  # Variable that will determine how many of each item a user is buying
    total = 0  # Variable that will hold the total cart price

    # Ask user if he would like to purchase anything today.
    user_action = str(input("Would you like to purchase anything in the store today? (y/n) "))

    # If user chooses yes, the code will proceed.
    if user_action == "Yes" or user_action == "yes" or user_action == "Y" or user_action == "y":
        print()
        print("Excellent! What would you like to purchase? We have:")

        for items in store.keys():  # Iterate over each key of the dictionary store
            print(store[items], items, "Available")  # Prints number in stock, item

        print()
        user_choice = str(input("Which items you would like? (Use commas to separate items and upper first letter): "))
        user_choice = user_choice.replace(',', "")  # Remove commas typed by user in product selection
        user_choice = user_choice.split()  # Create a list with the items chosen

        for product in user_choice:  # Iterate over item of the list
            if product not in store.keys():  # If user chooses an item not available, prompt error
                print("sorry, but we don't have", product, "in store.")

            else:
                print("How many", product, "would you like? ")
                quantity = int(input())  # If item is available, ask how many of each product

                if quantity > store[product]:  # If quantity exceeds, ask if buying the entire stock is ok
                    user_choice1 = input("Sorry, but that exceeds what we have in stock. "
                                         "Would you like to purchase the stock? (y/n) ")

                    if user_choice1 == "Yes" or user_choice1 == "yes" or user_choice1 == "Y" or user_choice1 == "y":
                        quantity = store[product]  # Make quantity equal to stock amount if user answers yes

                    elif user_choice1 == "No" or user_choice1 == "No" or user_choice1 == "N" or user_choice1 == "n":
                        # Ask how many of the stock would the user want if he answers no
                        quantity = int(input("Okay then. Choose how many that fits our stock. "))

                if product == "Phones":
                    price_list.append(phone_cost * quantity)
                elif product == "Cases":
                    price_list.append(case_cost * quantity)
                elif product == "Headphones":
                    price_list.append(headphone_cost * quantity)
                elif product == "Laptops":
                    price_list.append(laptop_costs * quantity)
                elif product == "Mouse":
                    price_list.append(mouse_cost * quantity)
                elif product == "Cables":
                    price_list.append(cables_cost * quantity)
                elif product == "Pendrive":
                    price_list.append(pendrive_cost * quantity)

                shopping_cart[product] = quantity  # Shopping cart will have product with quantity

        print("Your cart:", shopping_cart)

        # Gather total price
        for a in range(0, len(price_list)):  # Iterate over each element of price_list
            total += price_list[a]  # Add element value to total variable

        print("Your total is: $", total)

        # Confirm with user if ready to checkout
        user_action1 = input("Type y to checkout: ")

        if user_action1 == "Yes" or user_action1 == "yes" or user_action1 == "Y" or user_action1 == "y":
            # Update store dictionary so that it will reflect the new stock after purchase
            print("Thank you for doing business with us!")
            store = {key: store[key] - shopping_cart.get(key, 0) for key in store}
            if store[product] == 0:  # if a product reaches out of stock, remove from dict
                del store[product]  # Removing out of stock items from dict

        if not store:  # If store is empty, then exit the program
            print("Sorry, but we are completely sold out.")
            exit()

    #        elif user_action1 == "No" or user_action1 == "no" or user_action1 == "N" or user_action1 == "n":
    #            user_action2 = input("What would you like to remove? An item or quantity of items?")

    #            if user_action2 == "Item" or user_action2 == "item" or user_action2 == "I" or user_action2 == "i":
    #                print("Current shopping cart:", shopping_cart)
    #                choice = input("What item from your cart would you like to remove? ")
    #                if choice in shopping_cart:
    #                   del shopping_cart[choice]

    #                print("Updated shopping cart:", shopping_cart)
    #                # HELP: It is at this point where I got stuck with updating the price_list variable.

    # If user chooses no, the store will close.
    elif user_action == "No" or user_action == "no" or user_action == "N" or user_action == "n":
        print("We're sorry to see you leave. Goodbye!")
        exit()

    # If user enters something other than yes or no
    else:
        print("I'm sorry, what did you say?")
