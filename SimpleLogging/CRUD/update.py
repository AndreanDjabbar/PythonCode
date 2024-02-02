import os
from .utils import data_path, clear_data, activity_handler, error_handler
import logging

activity_logger = logging.getLogger(f"ACTIVITY LOGGER({__name__})")
# Create logger for activity log
error_logger = logging.getLogger(f"ERROR LOGGER({__name__})")
# Create logger for error log
activity_logger.setLevel(logging.INFO)
# Set level for activity logger
error_logger.setLevel(logging.ERROR)
# Set level for error logger
activity_logger.addHandler(activity_handler)
# Add handler for activity logger
error_logger.addHandler(error_handler)
# Add handler for error logger


def update_process(new_data:list):
    activity_logger.info("Clear Data")
    clear_data()
    # Delete all data from file data.txt
    with open(data_path, 'a', encoding="utf-8") as f:
        activity_logger.info("Open file data.txt")
        for data in new_data:
            new_data = f"{data[0]},{data[1]},{data[2]}\n"
            f.write(new_data)
    # Add new data to file data.txt
    activity_logger.info("Add new data to file")

def update_data():
    activity_logger.info("Start Update Data")
    is_loop = True
    while is_loop == True:
        os.system("cls")
        print("=" * 40)
        print("UPDATE DATA")
        print("=" * 40)
        all_data = []
        with open(data_path, 'r') as f:
            data = f.readline()
            while data:
                data = data.strip()
                data_splitted = data.split(',')
                all_data.append(data_splitted)
                data = f.readline()
        
        if len(all_data) == 0:
            activity_logger.warning("Warning Triggered! Data is Empty")
            print("\nData is Empty..")
        else:
            print(f"")
            for index, data in enumerate(all_data):
                name = data[0]
                age = data[1]
                message = data[2]
                print(f"No      : {index+1}")
                print(f"Name    : {name}")
                print(f"Age     : {age}")
                print(f"Message : {message}\n")
        if len(all_data) == 0:
            activity_logger.warning("Warning Triggered! Data is Empty")
            print("Data is Empty..")
            input("Enter to continue.. ")
            break
        else:
            try:
                target_index = int(input(f"Choose index data for update[1-{len(all_data)}]: "))
            except:
                error_logger.error("Error caused by inputting non-integer format")
                os.system("cls")
                print("Please input on integer format.... ")
                input("Enter to continue... ")

            if target_index < 1 or target_index > len(all_data):
                activity_logger.warning(f"Warning Triggered! target index {target_index} is not exist")
                os.system("cls")
                print(f"Data with index {target_index} is not Exist...")
                input("Enter to continue... ")
            else:
                os.system("cls")
                data_target = all_data[target_index-1]
                name = data_target[0]
                age = data_target[1]
                message = data_target[2]
                print("CURRENT DATA: \n")
                print(f"Name    : {name}")
                print(f"Age     : {age}")
                print(f"Message : {message}\n")

                while True:
                    name = input("Please input new Name[minimum 8 char]: ")
                    if len(name) < 8:
                        print("Please input minimum 8 characters..")
                        input("Enter to continue... ")
                        print("\n")
                    else:
                        break
                while True:
                    try:
                        age = int(input("Please input new age: "))
                    except:
                        error_logger.error("Error caused by inputting non-integer format")
                        os.system("cls")
                        print("Please input on integer format...")
                        input("Enter to continue.. ")
                    if age < 6:
                        activity_logger.warning(f"Warning Triggered! inputted age is {age}")
                        os.system("cls")
                        print("Minimum Age is 6")
                        input("Enter to continue.. ")
                        print("\n")
                    else:
                        break
                
                message = input("Please input new message: ")
                data_target[0] = name
                data_target[1] = age
                data_target[2] = message
                all_data[target_index-1] = data_target
                
                os.system("cls")
                print("NEW DATA: \n")
                print(f"Name    : {name}")
                print(f"Age     : {age}")
                print(f"Message : {message}\n")
                update_option = input("Are you sure for update the data[y/n]?: ")
                if update_option == 'y' or update_option == 'Y':
                    activity_logger.info("Update Data Successfully")
                    os.system("cls")
                    print("Update Successfull..\n")
                    update_process(all_data)
                    # Update processing

        input("Enter to continue.. ")
        activity_logger.info("Update Data Ended")
        break