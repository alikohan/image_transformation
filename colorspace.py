from PIL import Image
import math

def convert(pixels, width, height, type, image, fileName):
    type = type.upper()
    if not (type == "GRAYSCALE" or type == "BLACKANDWHITE"):
        return
    for i in range(width):
        for j in range(height):
            # value = int(math.sqrt((pixels[i, j][0]) ** 2 + (pixels[i, j][1]) ** 2 + (pixels[i, j][2]) ** 2) * 255/ 441) #euclidean distance
            value = int((pixels[i, j][0] + pixels[i, j][1] + pixels[i, j][2]) / 3)
            # for grayscale
            if type == "GRAYSCALE":
                pixels[i, j] = (value, value, value) # Set the RGB channels value of the image (tuple)
            # for black and white
            if type == "BLACKANDWHITE":
                if value & 128: # if value >= 128:
                    pixels[i, j] = (255, 255, 255) # Set the RGB channels value of the image (tuple)
                else:
                    pixels[i, j] = (0, 0, 0) # Set the RGB channels value of the image (tuple)
    image.save(fileName.replace(".jpg", "") + "_" + type + ".jpg")