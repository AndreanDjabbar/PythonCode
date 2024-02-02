import os
from .utils import data_path, activity_handler, error_handler
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

def add_to_file(data:str):
    activity_logger.info("Adding Data to file")
    with open(data_path, "a", encoding="utf-8") as f:
        f.write(data)
    # Write data into file data.txt

def add_data():
    activity_logger.info("Start Create Data")
    is_loop = True
    while is_loop == True:
        os.system("cls")
        print("=" * 40)
        print("CREATE DATA")
        print("=" * 40)

        while True:
            name = input("\nPlease input your Name[minimum 8 char]: ")
            if len(name) < 8:
                activity_logger.warning(f"Warning Triggred! name consist {len(name)} character")
                os.system("cls")
                print("Please input minimum 8 characters..")
                input("Enter to continue... ")
                print("\n")
            else:
                break
        while True:
            try:
                age = int(input("Please input your age: "))
            except:
                error_logger.error("Error caused by inputting non-integer format")
                os.system("cls")
                print("Please input on integer format...")
                input("Enter to continue.. ")
            if age < 6:
                os.system("cls")
                activity_logger.warning(f"Warning Triggred! age inputted is {age} years old")
                print("Minimum Age is 6")
                input("Enter to continue.. ")
                print("\n")
            else:
                break
        
        message = input("Please input the message: ")
        new_data = f"{name},{age},{message}\n"
        add_to_file(new_data)

        os.system("cls")
        activity_logger.info("Add Data Succesfull")
        print("Add Data Success..")
        continue_option = input("Continue for add data(y/n)?: ")
        if continue_option == 'n' or continue_option == 'N':
            activity_logger.info("Creating Data Ended")
            break
        else:
            activity_logger.info("Continue creating data")