import os
from utils import Ip
from data import continue_program
from input_ip import checking_Ip

def menu_option():
    os.system("cls")
    print("===== Welcome To Ip Calculator =====\n")
    print("1. Set Ip")
    print("2. Edit Ip")
    print("3. Calculate Ip")
    print("4. Exit\n")

def menu():
    is_ip_exist = False
    is_looping = True
    while is_looping:
        option = 0
        while True:
            menu_option()
            try:
                temp_option = int(input("Input option (1 - 4): "))
                if temp_option >= 1 and temp_option < 5:
                    option = temp_option
                    break

                else:
                    os.system("cls")
                    print("==== Please input option in range (1 - 4) ====\n")
                    continue_program()

            except:
                os.system("cls")
                print("==== Please input on integer format ====\n")
                continue_program()

        match option:
            case 1:
                is_looping_input_ip = True
                while is_looping_input_ip:
                    os.system("cls")
                    ip = input("input ip: ")
                    check_ip = checking_Ip(ip)

                    if check_ip == True:
                        is_ip_exist = True
                        data1 = Ip(ip)
                        break

                    else:
                        while True:
                            os.system("cls")
                            print("==== ERROR ====")
                            try:
                                print("\n1. Continue Input Ip")
                                print("2. Exit from input ip\n")
                                ip_input_option = int(input("Choose option (1 - 2): "))
                                
                                if ip_input_option == 1:
                                    break

                                elif ip_input_option == 2:
                                    is_looping_input_ip = False
                                    break
                                
                                else:
                                    os.system("Please input on range (1 - 2)...")
                                continue_program()

                            except:
                                os.system("cls")
                                print("Please input on integer format")
                                continue_program()
            case 2:
                if is_ip_exist:
                    is_looping_edit_ip = True
                    while is_looping_edit_ip:
                        os.system("cls")
                        try:
                            print("1. Reset Ip")
                            print("2. Set Subnet")
                            print("3. Exit from edit menu\n")
                            edit_ip_option = int(input("Choose option (1 - 3): "))

                            if edit_ip_option == 1:
                                del data1
                                is_ip_exist = False
                                os.system("cls")
                                print("==== Reset Ip successful ====\n")
                                continue_program()
                                break
                            
                            elif edit_ip_option == 2:
                                os.system("cls")
                                while True:
                                    os.system("cls")
                                    subnet_num = int(input("Input subnet (18 - 32): "))
                                    
                                    if subnet_num < 18 or subnet_num > 32:
                                        os.system("cls")
                                        print("==== Please input on range(18 - 32) ====\n")
                                        continue_program()
                                    else:
                                        os.system("cls")
                                        subnet = f"/{subnet_num}"
                                        data1.set_subnet(subnet)
                                        print("==== Set Subnet Completed ====\n")
                                        continue_program()
                                        is_looping_edit_ip = False
                                        break

                            elif edit_ip_option == 3:
                                break

                        except:
                            os.system("cls")
                            print("==== Please input on integer format ====\n")
                            continue_program()
                
                else:
                    os.system("cls")
                    print("==== Ip is not exist..please set ip first ====\n")
                    continue_program()

            
            case 3:
                if is_ip_exist == True:
                    os.system("cls")
                    data1.info()
                    is_looping_info_ip = True

                    while is_looping_info_ip:
                        info_looping_option = input("\nContinue Program ? (y/n): ")

                        if info_looping_option == 'n' or info_looping_option == 'N':
                            is_looping = False
                            break
                        else:
                            is_looping_info_ip = False
                
                elif is_ip_exist == False:
                    os.system("cls")
                    print("==== Ip is not exist..please set ip first ====\n")
                    continue_program()
                
            case 4:
                is_looping = False

        
    os.system("cls")
    print("======= Thank you and have a nice day =======\n")


def main():
    menu()


if __name__ == "__main__":
    main()
