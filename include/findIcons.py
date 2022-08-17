from ast import Str
import pyautogui
from PIL import Image, ImageDraw 

class icon:
    memories = 0
    takeSnap = 1
    filters = 2
    search = 3

def findMinMax(cordList, XY : str) -> tuple:
    min, max = 10000, 0

    XY = XY.lower()

    if XY == "x":
        for i, val in enumerate(cordList):
            x, y = cordList[i]
            if x > max:
                max = x
            elif x < min:
                min = x
    else:
        for i, val in enumerate(cordList):
            x, y = cordList[i]
            if y > max:
                max = y
            elif x < min:
                min = y


    print("Min: %d\nMax: %d" %(min, max))

    return (min, max)


def findWhitePixels(im : Image) -> list:
    width, height = im.size
    whiteCordsList = []

    for y in range(0, height):
        for x in range(0, width):
            RGBdata = im.getpixel((x, y))
            r, g, b, a = RGBdata
            if (r > 230 and g > 230 and b > 230):
                whiteCordsList.append((x, y))

    return whiteCordsList

def printPixels(cordList, im):
    newImg = im
    for i, val in enumerate(cordList):
        newImg.putpixel(cordList[i], (155, 155, 55))
    
    newImg.show()

allIconList = []

def editThreeSections():
    global allIconList

    min, max = findMinMax(allIconList[icon.memories], "x")
    oneHalf = (max + min) / 2
    tmpList = []

    for i, val in enumerate(allIconList[icon.memories]):
        x, y = allIconList[icon.memories][i]
        if x < oneHalf:
            tmpList.append(allIconList[icon.memories][i])

    allIconList[icon.memories] = tmpList

    min, max = findMinMax(allIconList[icon.filters], "x")
    oneHalf = (max + min) / 2
    tmpList = []

    for i, val in enumerate(allIconList[icon.filters]):
        x, y = allIconList[icon.filters][i]
        if x > oneHalf:
            tmpList.append(allIconList[icon.filters][i])

    allIconList[icon.filters] = tmpList


def findFirstThreeIcons(whiteCordList, img):
    width, height = img.size
    bottomWhitePixelsCords = []

    for i, val in enumerate(whiteCordList):
        x, y = whiteCordList[i]
        if y > height * 3 / 4:
            bottomWhitePixelsCords.append(whiteCordList[i])

    min, max = findMinMax(bottomWhitePixelsCords, "x")
    thirdLength = (max - min) / 3


    global allIconList

    allIconList = [[], [], []]
    thirdSection = 0

    for i, val in enumerate(bottomWhitePixelsCords):
        x, y = bottomWhitePixelsCords[i]

        for thirdSection in range(0, 3):
            if (x > min + (thirdLength * thirdSection) and 
            x < min + (thirdLength * (thirdSection + 1))):
                allIconList[thirdSection].append(bottomWhitePixelsCords[i])
        
    editThreeSections()


# def takeCroppedScreenShotOfIcon(cordList):

 


def main():
    imgPath = 'phone1/phone1.png'
    img = Image.open(imgPath)
    width, height = img.size
    global allIconList

    whitePixelsCords = findWhitePixels(img)

    findFirstThreeIcons(whitePixelsCords, img)

    printPixels(allIconList[icon.filters], img)


if __name__ == "__main__":
    main()