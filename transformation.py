from math import sqrt
from math import log

def transformationPlot(pixels, width, height, function, image):
    temp = [0, 0, 0]
    code0 = "if " + function[3:] + " > 255:\n\ttemp[0] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[0] = 0\nelse:\n\t" + "temp[0] = " + function[3:]
    code1 = "if " + function[3:] + " > 255:\n\ttemp[1] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[1] = 0\nelse:\n\t" + "temp[1] = " + function[3:]
    code2 = "if " + function[3:] + " > 255:\n\ttemp[2] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[2] = 0\nelse:\n\t" + "temp[2] = " + function[3:]
    code0 = code0.replace("a", "pixels[i, j][0]")
    code1 = code1.replace("a", "pixels[i, j][1]")
    code2 = code2.replace("a", "pixels[i, j][2]")
    for i in range(width):
        for j in range(height):
            exec(code0)
            exec(code1)
            exec(code2)
            pixels[i, j] = (int(temp[0]), int(temp[1]), int(temp[2]))
    image.show()

def transformationPlotPiecewise(pixels, width, height, function, image):
    ranges = []
    formulas = []
    rangeTemp = "" # range string for extractRange parameter
    formulaTemp = ""
    i = 0
    while i < len(function):
        if function[i] == "[":
            formulas.append(formulaTemp[1:])
            formulaTemp = ""
            while function[i] != "]":
                rangeTemp += function[i]
                i += 1
            rangeTemp += function[i]
            ranges.append(extractRange(rangeTemp))
            i += 1
        rangeTemp = ""
        formulaTemp += function[i]
        i += 1

    formulas.append(formulaTemp[1:])
    formulas.pop(0)
    print("ranges : ", ranges)
    print("forumulas : ", formulas)

    codes = []
    for formula in formulas: # generate codes
        temp = [0, 0, 0]
        code0 = "if " + formula[3:] + " > 255:\n\ttemp[0] = 255\n" + "elif " + formula[3:] + " < 0:\n\ttemp[0] = 0\nelse:\n\t" + "temp[0] = " + formula[3:]
        code1 = "if " + formula[3:] + " > 255:\n\ttemp[1] = 255\n" + "elif " + formula[3:] + " < 0:\n\ttemp[1] = 0\nelse:\n\t" + "temp[1] = " + formula[3:]
        code2 = "if " + formula[3:] + " > 255:\n\ttemp[2] = 255\n" + "elif " + formula[3:] + " < 0:\n\ttemp[2] = 0\nelse:\n\t" + "temp[2] = " + formula[3:]
        code0 = code0.replace("a", "pixels[i, j][0]")
        code1 = code1.replace("a", "pixels[i, j][1]")
        code2 = code2.replace("a", "pixels[i, j][2]")
        codes.append([code0, code1, code2])
    for i in range(width):
        for j in range(height):
            for k in range(len(ranges)):
                if pixels[i, j][0] >= ranges[k][0] and pixels[i, j][0] < ranges[k][1]: # check range
                    exec(codes[k][0])
                    pixels[i, j] = (int(temp[0]), pixels[i, j][1], pixels[i, j][2])
                if pixels[i, j][1] >= ranges[k][0] and pixels[i, j][1] < ranges[k][1]:
                    exec(codes[k][1])
                    pixels[i, j] = (pixels[i, j][0], int(temp[1]), pixels[i, j][2])
                if pixels[i, j][2] >= ranges[k][0] and pixels[i, j][2] < ranges[k][1]:
                    exec(codes[k][2])
                    pixels[i, j] = (pixels[i, j][0], pixels[i, j][1], int(temp[2]))
    image.show()


def extractRange(str):
    str = str[1:-1]
    ranges = str.split(",")
    ranges[0], ranges[1] = int(ranges[0]), int(ranges[1])
    return ranges

def testTransformationPlot(pixels, function):
    try:
        temp = [0, 0, 0]
        code0 = "if " + function[3:] + " > 255:\n\ttemp[0] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[0] = 0\nelse:\n\t" + "temp[0] = " + function[3:]
        code1 = "if " + function[3:] + " > 255:\n\ttemp[1] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[1] = 0\nelse:\n\t" + "temp[1] = " + function[3:]
        code2 = "if " + function[3:] + " > 255:\n\ttemp[2] = 255\n" + "elif " + function[3:] + " < 0:\n\ttemp[2] = 0\nelse:\n\t" + "temp[2] = " + function[3:]
        # print(code0)
        code0 = code0.replace("a", "pixels[i, j][0]")
        code1 = code1.replace("a", "pixels[i, j][1]")
        code2 = code2.replace("a", "pixels[i, j][2]")
        # print(code0)
        i = 0
        j = 0
        exec(code0)
        exec(code1)
        exec(code2)
        pixels[i, j] = (int(temp[0]), int(temp[1]), int(temp[2]))
        return 1
    except:
        return 0
