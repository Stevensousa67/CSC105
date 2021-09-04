# When you scan in images using a scanner they may have lots of noise due to dust particles on the image itself
# or the scanner itself, or the images may even be damaged. One way of eliminating this noise is to replace each pixel
# by the median value of the pixels surrounding it.
# Steven Sousa - Exercise 14 - 10/28/2020

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())


def reducenoise(img):
    """This function will reduce the noise of a picture using median algorithm"""
    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            p = [[img.getPixel(col, row),
                  img.getPixel(col + 1, row),
                  img.getPixel(col + 2, row)],

                 [img.getPixel(col, row + 1),
                  img.getPixel(col + 1, row + 1),
                  img.getPixel(col + 2, row + 1)],

                 [img.getPixel(col, row + 2),
                  img.getPixel(col + 1, row + 2),
                  img.getPixel(col + 2, row + 2)]
                 ]

            




reducenoise(img)
img.draw(win)
win.exitonclick()
