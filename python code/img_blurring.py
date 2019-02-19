import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel
        rand_i = random.randint(-1, 1)
        rand_j = random.randint(-1, 1)
        new_p = img.getPixel(i+rand_i, j+rand_j)
        new_img.setPixel(i, j, new_p)
        # TODO: in the new image, set this pixel's color to the neighbor's color

new_img.draw(win)
win.exitonclick()
