import os
import pandas
from . import view
from . import database

def update_data():

    while True:
        data_pandas = pandas.read_csv(database.file_name, sep=',')
        len_of_data = len(data_pandas)
        os.system("cls")
        if len_of_data == 0:
            os.system("cls")
            print("Data Empty...")
            continue_program = input("Click Enter to continue: ")
            break 
        
        view.view_data()
        try:
            choose_index = int(input(f"\nChoose the data number for update(1-{len_of_data}): "))
            if choose_index < 1 or choose_index > len_of_data:
                os.system("cls")
                print("Please choose existed data number..")
                continue_program = input("Click enter to continue: ")
            
            else:
                os.system("cls")
                data_pandas = pandas.read_csv(database.file_name)
                data_index_name = data_pandas.loc[choose_index - 1]['Name']
                data_index_id = data_pandas.loc[choose_index - 1]['Id']
                data_index_major = data_pandas.loc[choose_index - 1]['Major']
                data_index_age = data_pandas.loc[choose_index - 1]['Age']

                print(f"\nData: ")
                print(f"1. Name   : {data_index_name}")
                print(f"2. Id     : {data_index_id}")
                print(f"3. Major  : {data_index_major}")
                print(f"4. Age    : {data_index_age}")
                
                index_update = int(input("\n Choose the data index for update(1-4): "))

                if index_update < 1 or index_update > 4:
                    os.system("cls")
                    print("Please choose existed data number..")
                    continue_program = input("Click enter to continue: ")

                else:
                    os.system("Cls")

                    if index_update == 1:
                        print(f"Old name: {data_index_name}\n")
                        new_name = input("Input new name for data: ")
                        confirmation = input("\nAre your sure want to update this data? (y/n): ")

                        if confirmation == 'y' or confirmation == 'Y':
                            data_pandas.loc[choose_index-1, "Name"] = new_name

                    elif index_update == 2:
                        print(f"Old id: {data_index_id}\n")
                        new_id = input("Input new id for data: ")
                        confirmation = input("\nAre your sure want to update this data? (y/n): ")

                        if confirmation == 'y' or confirmation == 'Y':
                            data_pandas.loc[choose_index-1, "Id"] = new_id

                    elif index_update == 3:
                        print(f"Old major: {data_index_major}\n")
                        new_major = input("Input new major for data: ")
                        confirmation = input("\nAre your sure want to update this data? (y/n): ")

                        if confirmation == 'y' or confirmation == 'Y':
                            data_pandas.loc[choose_index-1, "Major"] = new_major

                    elif index_update == 4:
                        print(f"Old age: {data_index_age}\n")
                        new_age = int(input("Input new age for data: "))

                        if new_age < 0:
                            os.system("cls")
                            print("Minimum amount is 0")
                            continue_program = input("Click enter to continue: ")
                        else:
                            confirmation = input("\nAre your sure want to update this data? (y/n): ")
                            if confirmation == 'y' or confirmation == 'Y':
                                data_pandas.loc[choose_index-1, "Age"] = new_age
                    
                    data_pandas.to_csv(database.file_name, index=False)
                    os.system("cls")
                    print("Update Succesfull")
                    is_continue = input("\nContinue updating? (y/n): ")
                    if is_continue == 'n' or is_continue == 'N':
                        break

                    


        except:
            os.system("cls")
            print("\nInvalid Format\n")
            continue_program = input("Click enter to continue: ")


