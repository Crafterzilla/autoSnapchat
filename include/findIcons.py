import pyautogui
from PIL import Image, ImageDraw 

class icon:
    memories = 0
    takeSnap = 1
    filters = 2
    search = 3

def findPartLength(cordList) -> int:
    # Divide the bottom half into three section with the memories icon 
    # least x, and the the smile greastest x

    minX, maxX = 10000, 0

    for i, val in enumerate(cordList):
        x, y = cordList[i]
        if x > maxX:
            maxX = x
        elif x < minX:
            minX = x

    print("MinX: %d\nMaxX: %d" %(minX, maxX))

    partLength = (maxX - minX) / 3

    print("Length: %d" % partLength)

    return round(partLength), (minX, maxX)

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


def findFirstThreeIcons(whiteCordList, img):
    width, height = img.size
    bottomWhitePixelsCords = []

    for i, val in enumerate(whiteCordList):
        x, y = whiteCordList[i]
        if y > height * 3 / 4:
            bottomWhitePixelsCords.append(whiteCordList[i])

    thirdLength, minmax = findPartLength(bottomWhitePixelsCords)
    global allIconList

    allIconList = [[], [], []]
    thirdSection = 0

    for i, val in enumerate(bottomWhitePixelsCords):
        x, y = bottomWhitePixelsCords[i]
        minimum, maximum = minmax

        # if x > 99 and x < 295:
        #     allIconList[thirdSection].append(bottomWhitePixelsCords[i])
        for thirdSection in range(0, 3):
            if (x > minimum + (thirdLength * thirdSection) and 
            x < minimum + (thirdLength * (thirdSection + 1))):
                allIconList[thirdSection].append(bottomWhitePixelsCords[i])

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