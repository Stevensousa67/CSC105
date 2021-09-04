# Write a function to convert an image to black and white.
# Steven Sousa - Exercise 9 - 10/26/2020

import image

img = image.Image("luther.jpg")                         # Imports picture file
win = image.ImageWin(img.getWidth(), img.getHeight())   # Sets window to picture size


def convert_to_blacknwhite(rgb):
    """This function will convert a picture to black and white."""
    threshold = 127                              # 128 is half of 256. It is the middle of black and white
    for col in range(img.getWidth()):            # Goes through every column of the picture
        for row in range(img.getHeight()):       # Goes through every row of the picture
            p = img.getPixel(col, row)           # Grabs a pixel in the current location

            red = p.getRed()                     # red variable becomes that pixel's red value
            green = p.getGreen()                 # green variable becomes that pixel's green value
            blue = p.getBlue()                   # blue variable becomes that pixel's blue value

            if red > threshold or green > threshold or blue > threshold:  # if any color is above 127 set pixel to black
                p.setRed(255)
                p.setGreen(255)
                p.setBlue(255)
            else:                   # if not 127, set pixel to white
                p.setRed(0)
                p.setGreen(0)
                p.setBlue(0)

            newpixel = image.Pixel(p.getRed(), p.getGreen(), p.getBlue())   # newpixel has modified values
            img.setPixel(col, row, newpixel)    # Place new pixel where original pixel was


convert_to_blacknwhite(img)  # Call black and white function
img.draw(win)  # draws picture
win.exitonclick()
