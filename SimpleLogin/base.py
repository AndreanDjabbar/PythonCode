import os
import datetime
import json

secret_key = "7OJ2edCZXUdiTi_yoG56qlW4eUG8nQl0nfGk-IRANrA=".encode("utf-8")
# Declare Secret key for encrypt and decrypt

def menu():
    print(40*"=")
    print("WELCOME TO BLABLA SITE")
    print(40*"=")
    print("\n1. Sign-in")
    print("2. Login")
    print("3. Exit\n")

def generate_data():
    try:
        with open("users.json", 'r') as f:
            data = json.load(f)
            # Make Sure users.json file is exist
    except:
        with open("users.json", 'w') as f:
            template = {
                "users":[]
            }
            template = json.dumps(template, indent=4)
            f.write(template)
            # Create users.json if users.json not exist

def generate_users():
    with open("users.json", "r") as f:
        users = json.load(f)
        return users
        # Return all data in users.json

def main_page(username:str):
    os.system("cls")
    # Clean terminal

    today_time = datetime.datetime.now().hour

    if today_time >= 3 and today_time <= 10:
        today_time = "Morning"
    elif today_time > 10 and today_time < 15:
        today_time = "Afternoon"
    elif today_time >= 15 and today_time <= 19:
        today_time = "Evening"
    else:
        today_time = "Night"

    print(f"Good {today_time} {username}...")
    print("I Hope you enjoy this site\n\n")
    input("Enter to continue... ")    