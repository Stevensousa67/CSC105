# Steven Sousa - Exercise 4 - 11/26/2020

import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.hideturtle()
breski.penup()
xcoor_list = []
ycoor_list = []

def plot_regression(coordinates):
    """This function will make the turtle go to the receiving xy coordinates"""
    breski.stamp()
    breski.goto(coordinates)


def axis(width, height):
    """This function will create the window using max/min xy coordinates"""
    



file = open("labdata.txt", "r")             # Open labdata.txt file

for line in file:                           # Iterate over each line of the file
    index = line.split()                    # Make each line a list

    for i in range(len(index)):             # Iterate over each element of the new list
        index[i] = int(index[i])            # Convert each element into a interger

    coordinates = index[0], index[1]        # Create xy coordinate system
    xcoor_list.append(coordinates[0])       # Append all x values into xcoor_list
    ycoor_list.append(coordinates[1])       # Append all y values into ycoor_list

print("Highest and Lowest X coordinate:", max(xcoor_list), min(xcoor_list))     # Print max/min x values
print("Highest and Lowest Y coordinates:", max(ycoor_list), min(xcoor_list))    # Print max/min y values

window.exitonclick()