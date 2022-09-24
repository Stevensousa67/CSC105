# This module will calculate sales tax of MA, RI, and NH based on price given by the user.
# Creators: Steven Sousa, Gabriele Narmontaite, Liam Benway, Patrick Leddy
# 4Cs, Python, 10-6-2020

def ma_state_tax(price):
    tax = price * .0625
    final_price = tax + price
    final_price = round(final_price, 2)
    return final_price


def ri_state_tax(price):
    tax = price * .07
    final_price = tax + price
    final_price = round(final_price, 2)
    return final_price


def nh_state_tax(price):
    tax = price * 0
    final_price = tax + price
    final_price = round(final_price, 2)
    return final_price
