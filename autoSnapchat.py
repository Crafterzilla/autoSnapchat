from include.phoneConfigMenu import configurePhones
from include.autoMenu import autoMenu

def initText():
    print("""
##########################
#AUTOSNAPCHAT VERSION 1.0#
##########################

Made by Osmar Rojas/Crafterzilla

Code in my github: https://github.com/Crafterzilla/autoSnapchat

IMPORTANT!!!
READ the README.md in the files or on github before using or else
this program will not function correctly

""")

def main():
    initText()
    while True:
        print("""
1.) AutoSnapchat menu
2.) Edit Phone Config
3.) Exit program
""")
        choice = 0
        while True:
            try:
                choice = int(input("Type in an option: "))
                break
            except ValueError:
                print("Please Type in an integer")
        
        match choice:
            case 1:
                autoMenu()
            case 2:
                configurePhones()
            case 3:
                break
            case _:
                print("Invaild option. Please an option from the ones above")

if __name__ == "__main__":
    main()