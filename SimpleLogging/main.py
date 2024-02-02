import os
from CRUD import create, update, delete, read, utils
import logging

activity_logger = logging.getLogger(f"ACTIVITY LOGGER({__name__})")
error_logger = logging.getLogger(f"ERROR LOGGER({__name__})")
activity_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)
activity_logger.addHandler(utils.activity_handler)
error_logger.addHandler(utils.error_handler)

def generate_file():
    activity_logger.info("Generate File data.txt")
    try:
        with open(utils.data_path, 'r') as f:
            data = f.readlines()
    except:
        with open(utils.data_path, 'w', encoding="utf-8")as f:
            f.write("")

def menu():
    os.system("cls")
    print("="*40)
    print("WELCOME TO SIMPLE LOGGING APP")
    print("="*40)
    print("\n")
    print("1. Add Data")
    print("2. View Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit\n")

def main():
    activity_logger.info("Start Program")
    generate_file()
    is_looping = True
    menu_option = 0
    while is_looping == True:
        menu()
        try:
            menu_option = int(input("Please choose menu[1-5]: "))
        except:
            error_logger.error("Error caused by inputting non-integer format")
            os.system("cls")
            print("Please input on integer format...")
            input("Enter to continue.. ")
            continue
        match(menu_option):
            case 1:
                create.add_data()
            case 2:
                read.read_data()
            case 3:
                update.update_data()
            case 4:
                delete.delete_data()
            case 5:
                is_looping = False
            case _:
                os.system("cls")
                print("Please input [1-6]..")
                input("Enter to continue... ")
                continue


if __name__ == "__main__":
    main()
    os.system("cls")
    print("Thankyou and have a nice day... ")
    activity_logger.info("Program Ended")