import os
from . import database

def view_data():
    with open(database.file_name, "r") as f:
        passed_first_data = f.readline()
        all_data = f.readlines()

        title_name = "Name"
        title_id = "Id"
        title_age = "Age"
        title_major = "Major"
        title_number = "No"
        print("." * 130)
        print(f"{title_number:5} | {title_name:30} | {title_id:30} | {title_major:30} | {title_age:10}")
        print("." * 130)

        for index, data in enumerate(all_data):
            data_list = data.split(',')
            name = data_list[0]
            data_id = data_list[1]
            major = data_list[2]
            age = data_list[3]
            format_data = f"{index+1:5} | {name:30} | {data_id:30} | {major:30} | {age:.10}"
            print(format_data, end="")
        print("." * 130)
    
