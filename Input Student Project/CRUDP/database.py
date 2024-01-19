import pandas as pd

file_name = "Data.csv"

def check_data():
    try:
        with open(file_name, "r") as f:
            all_data = f.readlines()

    except:
        title_name = "Name"
        title_Id = "Id"
        title_Age = "Age"
        title_Major = "Major"
        format_title = f"{title_name},{title_Id},{title_Major},{title_Age}\n"

        with open(file_name, "w", encoding='utf-8') as f:
            f.writelines(format_title)