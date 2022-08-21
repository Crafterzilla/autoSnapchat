import pyautogui
import keyboard
from PIL import Image
from phoneConfigMenu import listPhones
import time

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
    usernameBox = 11

def getUsers():
    victims = []

    print("For program to work, you must type in the recipient's username correctly")

    while True:
        user = input("Input exact username for person to send: ")

        isUsernameCorrect = input("\nIs the username {} correct? (y/n): ".format(user))
        isUsernameCorrect = isUsernameCorrect.upper()
        if isUsernameCorrect == "Y":
            victims.append(user)
        else:
            continue

        addMoreUsers = input("\nDo you want to add another user to send to? (y/n): ")
        addMoreUsers = addMoreUsers.upper()
        if addMoreUsers != "Y":
            break

    print("\nSending to these users: ")
    for i, val in enumerate(victims):
        print(victims[i])

    return victims

def choosePhone():
    phoneList = listPhones()

    choice = 0
    while True:
        choice = int(input("Choose a phone from the ones above: "))
        if choice > 0 and choice < len(phoneList):
            break
        else:
            print("Invaild option. Choose an option from the ones listed above")

    phoneName = phoneList[choice - 1].strip()
    return phoneName

def findCord(pathName):
    while True:
        pos = pyautogui.locateCenterOnScreen(pathName, confidence=0.8)
        if pos != None:
            return pos


def getCords(phoneName : str):
    pos = [[], [], [], [], [], [], [], [], [], [], [], []]

    print("""Move snapchat home page window to the top of all windows. 
It should like the first screenshot you took
""")

    input("""After you press enter, do not move window until program is shutdown.
Doing so will ruin all the calculations of the program. While the random interval and 
set time have a much lesser chance of getting banned,
understand that spamming can get your account
banned; I do not take resposibilty for that.

If you understand of all of the above, press enter to start autoSnapchat: """)

    while True:
        if pyautogui.locateOnScreen("phones/{}/Screenshots/phone1.png".format(phoneName), confidence=0.8) == None:
            print("Move snapchat screen to the top")
            time.sleep(0.5)
        else:
            break

    print("Finding and calculating coordinate position. Please wait...")

    pos[icon.memories] = findCord("phones/{}/icons/memoriesIcon.png".format(phoneName))

    pos[icon.takeSnap] = findCord("phones/{}/icons/takeSnapIcon.png".format(phoneName))

    pos[icon.filters] = findCord("phones/{}/icons/filtersIcon.png".format(phoneName))

    pos[icon.search] = findCord("phones/{}/icons/searchIcon.png".format(phoneName))

    pyautogui.click(pos[icon.search].x, pos[icon.search].y, interval=0.5)
    pyautogui.write("f_in202210", interval=0.25)

    pos[icon.cancel] = findCord("phones/{}/icons/cancelIcon.png".format(phoneName))
    
    img = Image.open("phones/{}/Screenshots/phone2.png".format(phoneName))
    width, height = img.size

    pos[icon.usernameBox] = (pos[icon.cancel].x, pos[icon.cancel].y + (height / 2))

    pyautogui.click(pos[icon.usernameBox][0], pos[icon.usernameBox][1])

    pos[icon.phone] = findCord("phones/{}/icons/phoneIcon.png".format(phoneName))

    pos[icon.videoCall] = findCord("phones/{}/icons/videoCallIcon.png".format(phoneName))

    pos[icon.arrowBack] = findCord("phones/{}/icons/arrowBackIcon.png".format(phoneName))

    pos[icon.camera] = findCord("phones/{}/icons/cameraIcon.png".format(phoneName))

    pos[icon.chatBox] = findCord("phones/{}/icons/chatBoxIcon.png".format(phoneName))

    pyautogui.click(pos[icon.camera].x, pos[icon.camera].y, interval=0.5)
    pyautogui.click(pos[icon.takeSnap].x, pos[icon.takeSnap].y, interval=0.5)

    pos[icon.send] = findCord("phones/{}/icons/sendIcon.png".format(phoneName))

    pyautogui.click(pos[icon.send].x, pos[icon.send].y, interval=0.5)
    pyautogui.click(pos[icon.arrowBack].x, pos[icon.arrowBack].y, interval=0.5)
    pyautogui.click(pos[icon.cancel].x, pos[icon.cancel].y, interval=0.5)


    print("To shutdown the program, press crtl + c")
    return pos

def autoSendChats():
    victimNames = getUsers()
    phoneName = choosePhone()

    textToSend = input("Write a message to send repeatedly: ")

    choice = 0
    while choice < 1 or choice > 2:
        print("""
How do you want to auto send texts?
1.) Send Randomly
2.) Send at a set time per day
3.) Fuck it...spam them HEHEEHEHEHEHEHE!!!!!!
4.) Go back
    """)
        choice = int(input("Type in choice number: "))
        class send:
            random = 1
            setTime = 2
            spamThem = 3
            goBack = 4

        match choice:
            case send.random:
                # autoSendChats()
                break
            case send.setTime:
                # addPhone()
                break
            case send.spamThem:
                print("Going Back")
                break
            case send.goBack:
                print("Going back")
                break
            case _:
                print("Invaild Option. Choose one of the options above")



def autoMenu():
    choice = 0
    while choice < 1 or choice > 2:
        print("""
AutoSnap Options:
1.) Auto send snaps
2.) Auto send chats
3.) Go back
    """)

        choice = int(input("Type in choice number: "))
        class Option:
            sendSnaps = 1
            sendChats = 2
            goBack = 3

        match choice:
            case Option.sendSnaps:
                autoSendChats()
                break
            case Option.sendChats:
                # addPhone()
                break
            case Option.goBack:
                print("Going Back")
                break
            case _:
                print("Invaild Option. Choose one of the options above")


# autoMenu()
getCords("GENY")