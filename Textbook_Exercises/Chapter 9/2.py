# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack,
# Pack, and Quack. This loop tries to output these names in order.
# prefixes = "JKLMNOPQ"
# suffix = "ack"
# for p in prefixes:
#     print(p + suffix)
# Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?
# Steven Sousa - Exercise 2 - 11/12/2020

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == 'O' or p == 'Q':    # Create conditional for letter O and Q
        suffix = 'uack'         # make suffix = 'quack'
        print(p + suffix)       # prints Ouack and Quack
        suffix = 'ack'          # return suffix to 'ack' so that Pack isn't modified to 'Puack'
    else:
        print(p + suffix)
