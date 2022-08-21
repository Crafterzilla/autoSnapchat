import pyautogui

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

    
def autoSendChats():
    victimNames = getUsers()

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


autoMenu()