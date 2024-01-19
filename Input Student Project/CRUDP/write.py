from . import database
import os

def create_data():
    while True:
        os.system("cls")
        name = input("Input Name  : ")
        data_id = input("Input Id    : ")
        major = input("Input Major : ")
        try:
            age = int(input("Input Age   : "))
            if age > 0:
                os.system("cls")
                format_data = f"{name},{data_id},{major},{age}\n"
                print("Your data: ", format_data)
                is_create = input("Are you sure to add this data? (y/n): ")

                if is_create == 'y' or is_create == 'Y':
                    with open(database.file_name, "a", encoding='utf-8') as f:
                        f.writelines(format_data)
                        os.system("cls")
                        first_data_is_exist = True
                        print("Add Data Successfull\n")     
                        break

                else:
                    is_continue = input("Continue program? (y/n): ")
                
                    if is_continue == 'n' or is_continue == 'N':
                        break

            else:
                os.system("cls")
                print("Error!! Minimum amount is 1")
                is_continue = input("Continue program? (y/n): ")
                if is_continue == 'n' or is_continue == 'N':
                    break

        except:
            print("Invalid format type")

