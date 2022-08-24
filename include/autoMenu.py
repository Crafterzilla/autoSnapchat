import pyautogui
import keyboard
from PIL import Image
from phoneConfigMenu import listPhones
import time
from datetime import datetime
import random


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
        if choice > 0 and choice <= len(phoneList):
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
    time.sleep(1.0)
    pyautogui.write("Team Snapchat", interval=0.25)

    pos[icon.cancel] = findCord("phones/{}/icons/cancelIcon.png".format(phoneName))
    
    img = Image.open("phones/{}/Screenshots/phone2.png".format(phoneName))
    width, height = img.size

    pos[icon.usernameBox] = ((pos[icon.search][0] + pos[icon.cancel][0]) / 2, pos[icon.cancel].y + (height / 2))

    pyautogui.click(pos[icon.usernameBox][0], pos[icon.usernameBox][1])

    pos[icon.phone] = findCord("phones/{}/icons/phoneIcon.png".format(phoneName))

    pos[icon.videoCall] = findCord("phones/{}/icons/videoCallIcon.png".format(phoneName))

    pos[icon.arrowBack] = findCord("phones/{}/icons/arrowBackIcon.png".format(phoneName))

    pos[icon.camera] = findCord("phones/{}/icons/cameraIcon.png".format(phoneName))

    pos[icon.chatBox] = findCord("phones/{}/icons/chatBoxIcon.png".format(phoneName))

    pyautogui.click(pos[icon.camera].x, pos[icon.camera].y, interval=1)
    time.sleep(0.5)
    pyautogui.click(pos[icon.takeSnap].x, pos[icon.takeSnap].y, interval=1)

    pos[icon.send] = findCord("phones/{}/icons/sendIcon.png".format(phoneName))

    pyautogui.click(pos[icon.send].x, pos[icon.send].y, interval=1)
    pyautogui.click(pos[icon.arrowBack].x, pos[icon.arrowBack].y, interval=1)
    pyautogui.click(pos[icon.cancel].x, pos[icon.cancel].y, interval=1)

    print("AutoSnapchat Start!!")
    print("To shutdown the program, press move mouse to the top-right corner of screen or type ctrl + c into terminal")
    return pos

def spamChats(victimNames, phoneName, textToSend):
    print("It is recommended for max speed to only go to one user")
    pos = getCords(phoneName)


    if len(victimNames) == 1:
        pyautogui.click(pos[icon.search].x, pos[icon.search].y, interval=1)
        pyautogui.write(victimNames[0], interval=0.25)
        time.sleep(1.0)
        pyautogui.click(pos[icon.usernameBox][0], pos[icon.usernameBox][1], interval=1)
        pyautogui.moveTo(pos[icon.chatBox].x, pos[icon.chatBox].y)
        while True:
            pyautogui.write(textToSend)
            pyautogui.press("enter")
    else:
        print("Spam only works for one user")

def printCurrentTime():
    #print current time in HH:MM AM/PM Time
    currentTime = datetime.now()
    currentTime = str(currentTime.time())

    tmpCurrent = ""
    for i in range(0, 5):
        tmpCurrent = tmpCurrent + currentTime[i]

    currentTime = tmpCurrent

    hour = int(currentTime[0] + currentTime[1])

    if hour == 0:
        newHour = 12
        currentTime = currentTime.replace(str(hour), str(newHour))
        currentTime += " AM"
    elif hour > 12:
        newHour = hour - 12
        currentTime = currentTime.replace(str(hour), str(newHour))
        currentTime += " PM"
    else:
        currentTime += " AM"
    print("Current time is {}\n".format(currentTime))

def getTimes():
    printCurrentTime()
    #Get times with very precise error checking
    times = []
    while True:
        while True:
            inputTime = input("Type in time you wish to send in (HH:MM AM) or (HH:MM PM) format: ")
            inputTime = inputTime.upper()

            try:
                hour = int(inputTime[0] + inputTime[1])
                min = int(inputTime[3] + inputTime[4])
                if len(inputTime) != 8 or inputTime[2] != ":":
                    print("Invaild format. Make sure to type in like this ex.(07:23 PM)")
                elif "PM" not in inputTime and "AM" not in inputTime:
                    print("You need to write either PM or AM at the end of the time")
                elif hour > 12 or min >= 60:
                    print("Type in a valid time")
                else:
                    times.append(inputTime)
                    break
            except ValueError:
                print("Please type in an integer for HH or MM")

        choice = input("Do you wish to add another time? y/n: ")
        choice = choice.upper()
        if choice == "N":
            break
    

    for i, timeString in enumerate(times):
        hour = int(timeString[0] + timeString[1])
        min = int(timeString[3] + timeString[4])

        if "PM" in timeString:
            hour += 12
        elif "AM" in timeString and hour == 12:
            hour = 0
        
        times[i] = (hour, min)

    return times

def getRandomTimes():
    randomAmount = 0
    while True:
        try:
            randomAmount = int(input("Type in amount of times to send messege per day: "))
            break
        except ValueError:
            print("Invaild Input. Type in an integer")

    times = []
    for i in range(0, randomAmount):
        ranHour = random.randint(0, 23)
        ranMin = random.randint(0, 59)
        times.append((ranHour, ranMin))

    return times
 
def sendChatsAtSetTimes(timesToSend, victimNames, phoneName, textToSend):
    while True:
        choice = input("Spam for a minute or send message once (1 or 2): ")
        if choice == "1" or choice == "2":
            break
        else:
            print("Invaild input. Choose 1 or 2")

    pos = getCords(phoneName)

    # print(timesToSend)
    currentTime = datetime.now()
    currentTime = str(currentTime.time())
    currentHour = int(currentTime[0] + currentTime[1])
    currentMinute = int(currentTime[3] + currentTime[4])

    print("{}:{}".format(currentHour, currentMinute))

    printCurrentTime()
    while True:
        currentTime = datetime.now()
        currentTime = str(currentTime.time())
        currentHour = int(currentTime[0] + currentTime[1])
        currentMinute = int(currentTime[3] + currentTime[4])

        for i, userTime in enumerate(timesToSend):
            if userTime[0] == currentHour and userTime[1] == currentMinute:
                for j, victim in enumerate(victimNames):
                    pyautogui.click(pos[icon.search].x, pos[icon.search].y, interval=0.75)
                    pyautogui.write(victim, interval=0.25)
                    time.sleep(1.0)
                    pyautogui.click(pos[icon.usernameBox][0], pos[icon.usernameBox][1], interval=0.75)
                    time.sleep(0.5)
                    pyautogui.write(textToSend, interval=0.25)
                    pyautogui.press("enter")
                    pyautogui.click(pos[icon.arrowBack].x, pos[icon.arrowBack].y, interval=0.5)
                    pyautogui.click(pos[icon.cancel].x, pos[icon.cancel].y, interval=0.5)
                if choice == "2":
                    time.sleep(60)

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
                randomTimes = getRandomTimes() 
                sendChatsAtSetTimes(randomTimes, victimNames, phoneName, textToSend)
                break
            case send.setTime:
                timesToSend = getTimes()
                sendChatsAtSetTimes(timesToSend, victimNames, phoneName, textToSend)
                break
            case send.spamThem:
                spamChats(victimNames, phoneName, textToSend)
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
                # autoSendChats()
                break
            case Option.sendChats:
                autoSendChats()
                break
            case Option.goBack:
                print("Going Back")
                break
            case _:
                print("Invaild Option. Choose one of the options above")


autoMenu()