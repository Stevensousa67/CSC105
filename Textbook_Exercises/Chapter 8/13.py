# Write a general pixel mapper function that will take an image and a pixel mapping function as parameters.
# The pixel mapping function should perform a manipulation on a single pixel and return a new pixel.
# Steven Sousa - Exercise 13 - 10/28/2020

import image

img = image.Image("luther.jpg")                             # Import file
win = image.ImageWin(img.getWidth(), img.getHeight())       # create window with file size


def PixelMapper(img, graycscale):
    """This function will send pixel by pixel to grayscale function."""
    width = img.getWidth()                                  # sets width variable to file width
    height = img.getHeight()                                # sets height variable to file height
    newimage = image.EmptyImage(width, height)              # create blank image with just captured width and height

    for col in range(width):                                # Go over every column in the image
        for row in range(height):                           # Go over every row in the image
            p = img.getPixel(col, row)                      # Grab pixel of that column and row
            newpixel = graycscale(p)                        # create newpixel by sending original to grayscale function
            newimage.setPixel(col, row, newpixel)           # place newpixel in column and row in newimage
    return newimage                                         # return new image once for loops are done


def grayscale(p):
    """This function will apply grayscale filter to picture."""
    colorsum = p.getRed() + p.getGreen() + p.getBlue()      # Add the RGB values of pixel p
    average = colorsum // 3                                 # create average by using // (int result)
    newpixel = image.Pixel(average, average, average)       # set new pixel RGB values to avg (red, green, blue)
    return newpixel                                         # returns newpixel to PixelMapper function.


newimage = PixelMapper(img, grayscale)
newimage.draw(win)

win.exitonclick()
