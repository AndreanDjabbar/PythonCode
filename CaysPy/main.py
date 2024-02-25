import os
from play import play
from history import create_file, history
from tutorial import tutorial

def menu():
    os.system("cls")
    print('*' * 50)
    print((' ' * 17) + "Welcome To CaysPy")
    print('*' * 50)
    print("1. Play Game")
    print("2. Tutorial")
    print("3. History")
    print("4. Exit")

def menu_validation(menu_option:int):
    match(menu_option):
        case 1:
            play()
        case 2:
            tutorial()
        case 3:
            history()
        
def main():
    is_looping = True
    menu_option = 0
    while is_looping:
        menu()
        try:
            menu_option = int(input("\nChoose[1-4]: "))
        except:
            os.system("cls")
            print("Please input on integer format and within range [1-4] !")
            input("Enter to continue.. ")
        if menu_option == 4:
            is_looping = False
        elif menu_option < 1 or menu_option > 4:
            os.system("cls")
            print("Please input within range [1-4] !")
            input("Enter to continue.. ")
        else:
            menu_validation(menu_option)
    os.system("cls")
    print("Thanks For Playing the Game! ")

if __name__ == "__main__":
    create_file()
    main()