from PIL import Image, ImageDraw 

class icon:
    memories = 0 #
    takeSnap = 1 #
    filters = 2 #
    search = 3 #
    cancel = 4 #
    phone = 5
    videoCall = 6
    arrowBack = 7
    camera = 8
    chatBox = 9
    send = 10

def findMinMax(cordList, XY : str) -> tuple:
    min, max = 10000, 0

    XY = XY.upper()

    if XY == "X":
        for i, val in enumerate(cordList):
            x, y = cordList[i]
            if x > max:
                max = x
            elif x < min:
                min = x
    elif XY == "Y":
        for i, val in enumerate(cordList):
            x, y = cordList[i]
            if y > max:
                max = y
            elif y < min:
                min = y
    else:
        return None

    # print("Min%s: %d\nMax%s: %d" %(XY, min, XY, max))

    return (min, max)

def findRGBPixels(im : Image, color : str) -> list:
    width, height = im.size
    RGBCordsList = []

    #supported colors
    white = (240, 240, 240)
    # black = (27, 27, 27)
    black = (56, 56, 56)

    grey1 = (232, 232, 232)
    grey2 = (242, 242, 242)

    color = color.lower()

    for y in range(0, height):
        for x in range(0, width):
            RGBdata = im.getpixel((x, y))
            r, g, b, a = RGBdata

            if color == "black":
                if (r < black[0] and g < black[1] and b < black[2]):
                    RGBCordsList.append((x, y))
            elif color == "white":
                if (r > white[0] and g > white[1] and b > white[2]):
                    RGBCordsList.append((x, y))
            elif color == "grey":
                if ((r > grey1[0] and r < grey2[0]) and (g > grey1[1] and g < grey2[1])
                and (b > grey1[2] and b < grey2[2])):
                    RGBCordsList.append((x, y))

    return RGBCordsList

def printPixels(cordList, im):
    newImg = im
    for i, val in enumerate(cordList):
        newImg.putpixel(cordList[i], (155, 155, 55))
    
    newImg.show()

allIconList = []

def editThreeSections(icon1, icon3):
    global allIconList

    min, max = findMinMax(allIconList[icon1], "x")
    oneHalf = (max + min) / 2
    tmpList = []

    for i, val in enumerate(allIconList[icon1]):
        x, y = allIconList[icon1][i]
        if x < oneHalf:
            tmpList.append(allIconList[icon1][i])

    allIconList[icon1] = tmpList

    min, max = findMinMax(allIconList[icon3], "x")
    oneHalf = (max + min) / 2
    tmpList = []

    for i, val in enumerate(allIconList[icon3]):
        x, y = allIconList[icon3][i]
        if x > oneHalf:
            tmpList.append(allIconList[icon3][i])

    allIconList[icon3] = tmpList


def findFirstThreeIcons(whiteCordList, img : Image):
    width, height = img.size
    bottomWhitePixelsCords = []

    for i, val in enumerate(whiteCordList):
        x, y = whiteCordList[i]
        if y > height * 3 / 4:
            bottomWhitePixelsCords.append(whiteCordList[i])

    min, max = findMinMax(bottomWhitePixelsCords, "x")
    thirdLength = (max - min) / 3


    global allIconList

    allIconList = [[], [], [], [], [], [], [], [], [], []]
    thirdSection = 0

    for i, val in enumerate(bottomWhitePixelsCords):
        x, y = bottomWhitePixelsCords[i]

        for thirdSection in range(0, 3):
            if (x > min + (thirdLength * thirdSection) and 
            x < min + (thirdLength * (thirdSection + 1))):
                allIconList[thirdSection].append(bottomWhitePixelsCords[i])
                break
        
    editThreeSections(icon.memories, icon.filters)

def takeCroppedScreenShotOfIcon(cordList, img : Image) -> Image:
    minX, maxX = findMinMax(cordList, "x")
    minY, maxY = findMinMax(cordList, "y")

    box = (minX, minY, maxX, maxY)
    newImg = img.crop(box)

    return newImg

def getSearchIcon(whiteCordList, img : Image):
    width, height = img.size
    searchIconPixelsCords = []

    for i, val in enumerate(whiteCordList):
        x, y = whiteCordList[i]
        if y < height / 2 and x < width / 2:
            searchIconPixelsCords.append(whiteCordList[i])

    return searchIconPixelsCords

def getCancelIcon(img : Image):
    blackPixelCords = findRGBPixels(img, "black")
    # printPixels(blackPixelCords, img)

    cancelIconCords = []
    width, height = img.size

    for i, val in enumerate(blackPixelCords):
        x, y = blackPixelCords[i]
        if x > width / 2 and y < height / 2:
            cancelIconCords.append(blackPixelCords[i])

    return cancelIconCords

def getArrowBackIcon(img : Image):
    blackPixelCords = findRGBPixels(img, "black")
    greyPixelCords = findRGBPixels(img, "grey")
    tmpCords = []
    width, height = img.size    

    #if there are width amount of x values that have the same y, remove all grey pixels above that y value

    previousY = greyPixelCords[0][1]
    xCounter = 0
    middleGreyY = 0
    for i, val in enumerate(greyPixelCords):
        x, y = greyPixelCords[i]
        if xCounter == width - 2:
            middleGreyY = y
            break
        elif previousY == y:
            xCounter += 1
        else:
            previousY = y
            xCounter = 0

    for i, val in enumerate(greyPixelCords):
        x, y = greyPixelCords[i]
        if y < middleGreyY and x > width / 2:
            tmpCords.append(greyPixelCords[i])
    
    greyPixelCords = tmpCords

    #remove any last lost remaining pixels
    
    for i in range(0, width):
        tmpCords = []
        for j, val in enumerate(greyPixelCords):
            x, y = greyPixelCords[j]
            if x == i:
                tmpCords.append(greyPixelCords[j])
        if len(tmpCords) < 5 and len(tmpCords) != 0:
            for j, val in enumerate(greyPixelCords):
                x, y = greyPixelCords[j]
                if x == i:
                    del greyPixelCords[j]

    # printPixels(greyPixelCords, img)

    greyMinX, greyMaxX = findMinMax(greyPixelCords, "x")
    greyMinY, greyMaxY = findMinMax(greyPixelCords, "y")

    tmpCords = []
    for i, val in enumerate(blackPixelCords):
        x, y = blackPixelCords[i]
        if y < greyMaxY and x > greyMinX:
            tmpCords.append(blackPixelCords[i])

    # printPixels(tmpCords, img)

    min, max = findMinMax(tmpCords, "x")
    thirdLength = (max - min) / 3

    global allIconList
    thirdSection = 0

    for i, val in enumerate(tmpCords):
        x, y = tmpCords[i]

        j = 0
        for thirdSection in range(icon.phone, icon.arrowBack + 1):
            if (x > min + (thirdLength * j) and 
            x < min + (thirdLength * (j + 1))):
                allIconList[thirdSection].append(tmpCords[i])
                break
            j += 1

def getCameraAndChatBox(img : Image):
    greyPixelCords = findRGBPixels(img, "grey")
    whitePixelCords = findRGBPixels(img, "white")
    #get rid of all grey pixels at the top

    width, height = img.size
    tmpPixelCords = []

    for i, val in enumerate(greyPixelCords):
        x, y = greyPixelCords[i]
        if y > height / 2 and x < width / 2:
            tmpPixelCords.append(greyPixelCords[i])

    greyPixelCords = tmpPixelCords
    minGreyY, maxGreyY = findMinMax(greyPixelCords, "y")

    #Get rid of top line of grey pixels
    tmpPixelCords = []
    for i, val in enumerate(greyPixelCords):
        x, y = greyPixelCords[i]
        if (y != minGreyY):
            tmpPixelCords.append(greyPixelCords[i])

    greyPixelCords = tmpPixelCords


    #edit whtie pixels accordingly
        #take away all pixels above and below grey bars
    minGreyY, maxGreyY = findMinMax(greyPixelCords, "y")
    tmpPixelCords = []
    for i, val in enumerate(whitePixelCords):
        x, y = whitePixelCords[i]
        if y > minGreyY and y < maxGreyY and x < width / 2:
            tmpPixelCords.append(whitePixelCords[i])

    whitePixelCords = tmpPixelCords
        #take way remaining last white pixels

    minWhiteX, maxWhiteX = findMinMax(whitePixelCords, "x")
    middleWhiteX = (minWhiteX + maxWhiteX) / 2

    tmpPixelCords = []
    for i, val in enumerate(whitePixelCords):
        x, y = whitePixelCords[i]
        if x > middleWhiteX:
            tmpPixelCords.append(whitePixelCords[i])

    whitePixelCords = tmpPixelCords

        #use remaining white pixels to seperate the two gray boxes

    minWhiteX, maxWhiteX = findMinMax(whitePixelCords, "x")
    middleWhiteX = (minWhiteX + maxWhiteX) / 2

    global allIconList
    for i, val in enumerate(greyPixelCords):
        x, y = greyPixelCords[i]
        if x > middleWhiteX:
            allIconList[icon.chatBox].append(greyPixelCords[i])
        else:
            allIconList[icon.camera].append(greyPixelCords[i])

def getIcons(phoneName : str):
    imgPath = ["", "", "", ""]
    for i, val in enumerate(imgPath):
        imgPath[i] = "phones/{}/Screenshots/phone{}.png".format(phoneName, str(i + 1))

    img = Image.open(imgPath[0])
    global allIconList

    whitePixelsCords = findRGBPixels(img, "white")

    findFirstThreeIcons(whitePixelsCords, img)

    #Get memories icon
    memoriesIcon = takeCroppedScreenShotOfIcon(allIconList[icon.memories], img)
    memoriesIcon.save("phones/{}/icons/memoriesIcon.png".format(phoneName))

    #Get take snap icon
    takeSnapIcon = takeCroppedScreenShotOfIcon(allIconList[icon.takeSnap], img)
    takeSnapIcon.save("phones/{}/icons/takeSnapIcon.png".format(phoneName))

    #Get filters icon
    filtersIcon = takeCroppedScreenShotOfIcon(allIconList[icon.filters], img)
    filtersIcon.save("phones/{}/icons/filtersIcon.png".format(phoneName))

    #Get search icon
    searchIconCords = getSearchIcon(whitePixelsCords, img)
    searchIcon = takeCroppedScreenShotOfIcon(searchIconCords, img)
    searchIcon.save("phones/{}/icons/searchIcon.png".format(phoneName))

    #get cancel icon
    img = Image.open(imgPath[1])
    cancelIconCords = getCancelIcon(img)
    cancelIcon = takeCroppedScreenShotOfIcon(cancelIconCords, img)
    cancelIcon.save("phones/{}/icons/cancelIcon.png".format(phoneName))

    #get arrowback icon
    img = Image.open(imgPath[2])
    getArrowBackIcon(img)

    arrowBackIcon = takeCroppedScreenShotOfIcon(allIconList[icon.arrowBack], img)
    arrowBackIcon.save("phones/{}/icons/arrowBackIcon.png".format(phoneName))

    #get phone icon
    phoneIcon = takeCroppedScreenShotOfIcon(allIconList[icon.phone], img)
    phoneIcon.save("phones/{}/icons/phoneIcon.png".format(phoneName))

    #get video call icon
    videoCallIcon = takeCroppedScreenShotOfIcon(allIconList[icon.videoCall], img)
    videoCallIcon.save("phones/{}/icons/videoCallIcon.png".format(phoneName))

    #get camera icon
    getCameraAndChatBox(img)
    cameraIcon = takeCroppedScreenShotOfIcon(allIconList[icon.camera], img)
    cameraIcon.save("phones/{}/icons/cameraIcon.png".format(phoneName))

    #get chatbox icon
    chatBoxIcon = takeCroppedScreenShotOfIcon(allIconList[icon.chatBox], img)
    chatBoxIcon.save("phones/{}/icons/chatBoxIcon.png".format(phoneName))

    #get send icon
    img = Image.open(imgPath[3])
    img.save("phones/{}/icons/sendIcon.png".format(phoneName))
