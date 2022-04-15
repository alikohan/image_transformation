from math import sqrt
from math import log

def transformationPlot(pixels, width, height, function, image):
    temp = [0, 0, 0]
    code0 = "if " + function[3:] + " > 255:\n\ttemp[0] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[0] = 0\nelse:\n\t" + "temp[0] = " + function[3:]
    code1 = "if " + function[3:] + " > 255:\n\ttemp[1] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[1] = 0\nelse:\n\t" + "temp[1] = " + function[3:]
    code2 = "if " + function[3:] + " > 255:\n\ttemp[2] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[2] = 0\nelse:\n\t" + "temp[2] = " + function[3:]
    for i in range(width):
        for j in range(height):
            code0 = code0.replace("a", "pixels[i, j][0]")
            code1 = code1.replace("a", "pixels[i, j][1]")
            code2 = code2.replace("a", "pixels[i, j][2]")
            exec(code0)
            exec(code1)
            exec(code2)
            pixels[i, j] = (int(temp[0]), int(temp[1]), int(temp[2]))
    image.show()

def testTransformationPlot(pixels, width, height, function):
    try:
        temp = [0, 0, 0]
        code0 = "if " + function[3:] + " > 255:\n\ttemp[0] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[0] = 0\nelse:\n\t" + "temp[0] = " + function[3:]
        code1 = "if " + function[3:] + " > 255:\n\ttemp[1] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[1] = 0\nelse:\n\t" + "temp[1] = " + function[3:]
        code2 = "if " + function[3:] + " > 255:\n\ttemp[2] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[2] = 0\nelse:\n\t" + "temp[2] = " + function[3:]
        # print(code0)
        i = 0
        j = 0
        code0 = code0.replace("a", "pixels[i, j][0]")
        code1 = code1.replace("a", "pixels[i, j][1]")
        code2 = code2.replace("a", "pixels[i, j][2]")
        # print(code0)
        exec(code0)
        exec(code1)
        exec(code2)
        pixels[i, j] = (int(temp[0]), int(temp[1]), int(temp[2]))
        return 1
    except:
        return 0