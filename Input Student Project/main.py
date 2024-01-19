import os
from CRUDP import check_data, create_data, view_data, update_data, delete, print_data

if __name__ == "__main__":
    check_data()
    while True:
        os.system("cls")
        print("." * 130)
        print("STUDENT OF BLABLABLA UNIVERSITY")
        print("." * 130)
        print("\nMenu: ")
        print("1. View Data")
        print("2. Add Data")
        print("3. Delete Data")
        print("4. Update Data")
        print("5. Print Data")
        print("6. Exit")

        try:
            option = int(input("\nInput menu(1-6): "))
            if option >= 1 and option <=6:
                match option:
                    case 1:
                        os.system("cls")
                        view_data()
                        is_continue = input("\nContinue? (y/n): ")
                        if is_continue == 'n' or is_continue == 'N':
                            break
                    
                    case 2:
                        os.system("cls")
                        create_data()

                    case 3:
                        os.system("cls")
                        delete()

                    case 4:
                        os.system("cls")
                        update_data()

                    case 5:
                        os.system("cls")
                        print_data()

                    case 6:
                        break

            else:
                print("Error...please input 1-6")

        except:
            print("Please input data on integer type")
    
    os.system("cls")
    print("Thank You...Have a good day")