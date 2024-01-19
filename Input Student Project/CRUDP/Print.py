import pandas
import os
from . import database

os.system("cls")

def print_data():
    
    data_pandas = pandas.read_csv(database.file_name)
    len_of_data = len(data_pandas)

    if len_of_data == 0:
        os.system("cls")
        print("Data Empty...")
        continue_program = input("Click Enter to continue: ")

    else:
        data_pandas = pandas.read_csv(database.file_name)
        file_target = input("Please input the name of file for print the data: ")
        print("\n1. Txt")
        print("2. Csv")
        try:
            file_type = int(input("Choose file type(1-2): "))
            if file_type > 0 and file_type < 3:
                if file_type == 1:
                    file_target = f"{file_target}.txt"
                    data_result = str(data_pandas)
                    os.system("cls")
                    with open(file_target, "w", encoding='utf-8') as f:
                        f.write(data_result)
                    print(f"\nData has been printed to \"{file_target}\"\n")

                elif file_type == 2:
                    file_target = f"{file_target}.csv"
                    data_pandas.to_csv(file_target, index=False)
                os.system("cls")
                print(f"\nData has been printed to \"{file_target}\"\n")
                continue_submit = input("Click enter to continue: ")
                
            else:
                os.system("cls")
                print("Input should be (1-2)")
        except:
            print("invalid data type")
