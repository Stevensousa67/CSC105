# Write a function to convert the image to grayscale.
# Steven Sousa - Exercise 8 - 10/26/2020

import image

img = image.Image("luther.jpg")     # imports file picture
win = image.ImageWin(img.getWidth(), img.getHeight())   # Creates a window with the picture size


def convert_to_grayscale(rgb):
    """This function will convert any image into grayscale"""
    for col in range(img.getWidth()):   # Go through every column of the picture
        for row in range(img.getHeight()):  # Go through every row of the picture
            p = img.getPixel(col, row)  # Grabs a specific pixel at the current column and row

            red = p.getRed()        # set red as the pixel red value
            green = p.getGreen()    # set green as the pixel green value
            blue = p.getBlue()      # set blue as the pixel blue value

            average = (red + green + blue) / 3  # Average the color of that pixel
            average = int(average)              # Use the int result
            redavg = average                    # set redavg as the average color
            greenavg = average                  # set greenavg as the average color
            blueavg = average                   # set blueavg as the average color

            newpixel = image.Pixel(redavg, greenavg, blueavg)   # Assign newpixel with the average values
            img.setPixel(col, row, newpixel)                    # Places newpixel in the original pixels place


convert_to_grayscale(img)   # Call function
img.draw(win)               # draws grayscale picture
win.exitonclick()
