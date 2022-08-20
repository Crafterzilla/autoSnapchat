import pyautogui
import os



def addPhone():
    with open("data/phones.txt", "r") as file:
        
        phoneList = file.readlines()
        phoneName = ""

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
    
    with open("data/phones.txt", "a") as file:
        file.write("\n" + phoneName)
        os.mkdir("phones/%s" % phoneName)
        os.mkdir("phones/%s/icons" % phoneName)
        os.mkdir("phones/%s/Screenshots" % phoneName)

    

    



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
