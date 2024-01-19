import os
import SIA


while True:
    os.system("cls")
    print("WELCOME TO ROCK PAPER SCISSORS GAME!!!!")
    SIA.show_menu()

    try:
        menu_option = int(input("\nChoose Menu: "))
        match(menu_option):
            case 1:
                SIA.play_game()
            
            case 2:
                SIA.tutorial_game()

            case 3:
                break

    except:
        os.system("cls")
        print("\nPlease input on integer format..")
        continue_button = input("enter to continue...")

os.system("cls")
print("Thank you.... and have a nice day :)")