import pyautogui
import os
from findIcons import getIcons


def addPhone():
    with open("data/phones.txt", "r") as file:
        
        phoneList = file.readlines()
        phoneName = ""

        #all of this to get phone name bruh
        while True:
            isNameInList = True
            print("Warning: Spaces, Apostrophes, and quotation marks are not allowed")
            phoneName = input("Type in a name for phone (Ex. Samsung_Galaxy, Pixel, etc.): ")
            phoneName = phoneName.upper()

            #check for invaild characters
            if "'" in phoneName:
                print("Invaild character (')\nType a different name\n")
                continue
            elif '"' in phoneName:
                print('Invaild character (")\nType a different name\n')
                continue
            elif ' ' in phoneName:
                print('Invaild character (Spaces not allowed)\nType a different name\n')
                continue

            # Check to see if name is already taken
            for i, val in enumerate(phoneList):
                if phoneName == phoneList[i] or phoneName + "\n" == phoneList[i]:
                    print("%s is an already taken name. Write a different name\n" % phoneName)
                    isNameInList = True
                    break
                else:
                    isNameInList = False
            #ensure user wants that name
            if isNameInList == False:
                choice = input("Is the Name %s fine (y/n): " % phoneName)
                choice = choice.upper()

                if choice == "Y":
                    break
    
    #make directories need for program to function
    with open("data/phones.txt", "a") as file:
        file.write("\n" + phoneName)
        os.mkdir("phones/%s" % phoneName)
        os.mkdir("phones/%s/icons" % phoneName)
        os.mkdir("phones/%s/Screenshots" % phoneName)

    #get file for program to function
    cwd = os.getcwd() + "/phones/" + phoneName
    print("""
For the program to work, you need to take four seperate screenshots
Those screenshots need to look as nearly closely similar as the ones shown in this directory:
{}/exampleScreenShots

The files need to be put in exactly the order shown and with exactly the name phone1.png, phone2.png, etc.
The program will extract all the pixel data needed for the bot to find right coordinates
Place those files into this directory:

{}/Screenshots
""".format(cwd, cwd))

    input("Once done press enter to continue and to check for files: ")
    
    areFilesThere = False
    while areFilesThere == False:
        for i in range (1, 5):
            try:
                file = open("phones/{}/Screenshots/phone{}.png".format(phoneName, str(i)), "r")
                file.close()
                areFilesThere = True
            except:
                print("Failed to open phone{}.png".format(str(i)))
                print("Retry placing the approperiate files into {}/Screenshots".format(cwd))
                input("Once done press enter to retry: ")
                areFilesThere = False
                break
        print()

    print("All files found, now creating all other necessary files...")
    getIcons(phoneName)
    print("{} profile created successfully!".format(phoneName))



def configurePhones():

    choice = 0
    while (choice < 1 or choice > 4):
        print("""
    1.) List Phones
    2.) Add Phone
    3.) Remove Phone
    4.) Reset A Phone Profile
    5.) Go Back

    """)

        choice = int(input("Type in choice number: "))

        class Option:
            List = 1
            AddPhone = 2
            RemovePhone = 3
            ResetPhone = 4
            GoBack = 5

        match choice:
            case Option.List:
                print("List")
                break
            case Option.AddPhone:
                print("Add")
                break
            case Option.RemovePhone:
                print("Renmove")
                break
            case Option.ResetPhone:
                print("Reset")
                break
            case Option.GoBack:
                print("Go BAck")
                break
            case _:
                print("Invaild Option. Choose one of the options above")








# configurePhones()
addPhone()
