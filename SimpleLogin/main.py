import os
from base import menu, generate_data
from login import login
from sign_in import sign_in

is_loop = True
menu_option = 0
generate_data()
# Check users.json is exist or no 

while is_loop == True:
    os.system("cls")
    # Clean terminal

    menu()

    try:
        menu_option = int(input("Choose Menu[1-3]: "))
    except:
        os.system("cls")
        print("Please Input on Integer Format...\n")
        input("Enter to Continue... ")
        continue

    if menu_option > 0 and menu_option < 4:
        match(menu_option):
            case 1:
                sign_in()
            case 2:
                login()
            case 3:
                is_loop = False
    else:
        os.system("cls")
        print("Please choose [1-3]....\n")
        input("Enter to Continue.... ")

os.system("cls")
# Clean terminal

print("Thankyou and Have a nice Day..")