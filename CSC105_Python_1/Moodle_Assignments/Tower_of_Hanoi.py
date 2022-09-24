# Tower of Hanoi Puzzle
# Credit to dilipjain0504, nidhi_biet from geeksforgeeks.org in aiding with the implementation.
# https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
# # Steven Sousa - 10/29/2020

def TowerOfHanoi(x, start, destination, auxiliary):
    """This function will solve the Tower of Hanoi puzzle"""
    # If game has 1 disk only, simply move it to the third pole
    if x == 1:
        print("Move disk 1 from source", start, "to destination", destination)
        return

    # Recursive call sending x - 1
    TowerOfHanoi(x - 1, start, auxiliary, destination)
    # Print current movement of disk #
    print("Move disk", x, "from source", start, "to destination", destination)
    # Recursive call again to move another disk to another pole
    TowerOfHanoi(x - 1, auxiliary, destination, start)


# Ask for disk quantity
diskquantity = int(input("How many disks for this game? "))

# Send the values to the function. A, B, and C are the poles
TowerOfHanoi(diskquantity, "Pole A", 'Pole B', 'Pole C')

# Steven Sousa note: I found this problem to be a bit hard to understand the concepts. I tried watching
# various videos on YouTube to understand the algorithm, but it still didn't click. I did understanding the
# problem in real life, but putting it in code is what caught me. I believe it's because I would get lost in
# double recursion calls.
