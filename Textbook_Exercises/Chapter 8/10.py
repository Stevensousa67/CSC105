# Sepia Tone images are those brownish colored images that may remind you of times past.
# The formula for creating a sepia tone is as follows:

# newR = (R × 0.393 + G × 0.769 + B × 0.189)
# newG = (R × 0.349 + G × 0.686 + B × 0.168)
# newB = (R × 0.272 + G × 0.534 + B × 0.131)

# Write a function to convert an image to sepia tone.
# Hint: Remember that rgb values must be integers between 0 and 255.
# Steven Sousa - Exercise 10 - 10/26/2020

import image

img = image.Image("luther.jpg")                             # Imports picture file
win = image.ImageWin(img.getWidth(), img.getHeight())       # Sets window to picture size


def convert_to_sepiatone(rgb):
    """This function will convert a picture to Sepia Tone"""
    for col in range(img.getWidth()):                       # Goes through every column of the picture
        for row in range(img.getHeight()):                  # Goes through every row of the picture
            p = img.getPixel(col, row)                      # Grabs a pixel in the current location

            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            # Apple the sepia tone formula on each pixel color
            newR = int(red * 0.393 + green * 0.769 + blue * 0.189)
            if newR > 255:  # If the product of the formula is above 255, the color gets set to 255
                newR = 255
            p.setRed(newR)

            newG = int(red * 0.349 + green * 0.686 + blue * 0.168)
            if newG > 255:
                newG = 255
            p.setGreen(newG)

            newB = int(red * 0.272 + green * 0.534 + blue * 0.131)
            if newB > 255:
                newB = 255
            p.setGreen(newB)

            newpixel = image.Pixel(newR, newG, newB)
            img.setPixel(col, row, newpixel)


convert_to_sepiatone(img)
img.draw(win)
win.exitonclick()
