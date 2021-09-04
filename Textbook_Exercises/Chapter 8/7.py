import image

img = image.Image("luther.jpg")     # imports the luther.jpg file
win = image.ImageWin(img.getWidth(), img.getHeight())   # sets the window with the file's size
img.draw(win)   # Draws in the window
img.setDelay(0)     # Removes animations

for row in range(img.getHeight()):  # goes over every row within the file
    for col in range(img.getWidth()):   # goes over every column within the file
        p = img.getPixel(col, row)  # grabs the pixel in the current column and row

        newred = 0                  # sets the red of that pixel to 0 (removes red)
        green = p.getGreen()        # green is that pixel's green value
        blue = p.getBlue()          # blue is that pixel's blue value

        newpixel = image.Pixel(newred, blue, green)  # newpixel will will replace the original pixel
        img.setPixel(col, row, newpixel)             # set newpixel into the new picture

img.draw(win)
win.exitonclick()
