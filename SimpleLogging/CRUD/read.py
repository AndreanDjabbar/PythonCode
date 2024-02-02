import os
from .utils import data_path, activity_handler
import logging

activity_logger = logging.getLogger(f"ACTIVITY LOGGER({__name__})")
# Create logger for activity log
activity_logger.setLevel(logging.INFO)
# Set level for activity logger
activity_logger.addHandler(activity_handler)
# Add handler for activity logger

def read_data():
    activity_logger.info("Start Read Data")
    print("=" * 40)
    print("READ DATA")
    print("=" * 40)
    os.system("cls")
    all_data = []
    with open(data_path, 'r') as f:
        activity_logger.info("Open File data.txt")
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
        print("\n")
        print(f"")
        for index, data in enumerate(all_data):
            name = data[0]
            age = data[1]
            message = data[2]
            print(f"No      : {index+1}")
            print(f"Name    : {name}")
            print(f"Age     : {age}")
            print(f"Message : {message}\n")
    activity_logger.info("Read Data Ended")
    input("\nEnter to continue... ")

