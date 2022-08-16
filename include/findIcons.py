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

    minX, maxX = cordList[0][0], cordList[0][1]

    for i, val in enumerate(cordList):
        x, y = cordList[i]
        if x > maxX:
            maxX = x
        elif x < minX:
            minX = x

    print("MinX: %d\nMaxX: %d" %(minX, maxX))

    partLength = (maxX - minX) / 3

    print("Length: %d" % partLength)

    return partLength

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



def main():
    imgPath = 'phone1/phone1.png'
    img = Image.open(imgPath)
    width, height = img.size

    whitePixelsCords = findWhitePixels(img)

    printPixels(whitePixelsCords, img)


if __name__ == "__main__":
    main()