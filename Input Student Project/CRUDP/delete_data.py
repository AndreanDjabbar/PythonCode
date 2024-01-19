from . import database
import pandas as pd
from . import view
import os

def delete():
    while True:
        data_pandas = pd.read_csv(database.file_name, sep=',')
        data_series = data_pandas.squeeze()
        len_of_data = len(data_pandas)

        if len_of_data == 0:
            os.system("cls")
            print("Data Empty...")
            continue_program = input("Click Enter to continue: ")
            break

        os.system("cls")
        view.view_data()
        try:
            index_data_for_delete = int(input(f"\nInput index of data for delete (1-{len_of_data}): "))
            if index_data_for_delete >= 0 and index_data_for_delete <= len_of_data:
                os.system("cls")
                is_agree = input("Are you sure for deleting this data ? (y/n): ")
                if is_agree == 'Y' or is_agree == 'y':
                    data_pandas = data_pandas.drop(index_data_for_delete-1, axis=0)
                    data_pandas.to_csv(database.file_name, index=False)
                    os.system("cls")
                    print("Delete Data Successfull")

        except:
            print("Invalid format")


        is_continue = input("\nContinue Deleting? (y/n): ")

        if is_continue == 'n' or is_continue == 'N':
            break


