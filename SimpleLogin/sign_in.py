import os
import getpass
from base import secret_key, generate_users
import json
from cryptography.fernet import Fernet as fr

def add_user(username:str, password:str):
    user_id = username + password
    fernet = fr(secret_key)

    user_id = fernet.encrypt(user_id.encode("utf-8"))
    password = fernet.encrypt(password.encode("utf-8"))
    # Encrypt user_id,password and encode from String into Bytes

    users = generate_users()
    # Get all_data from users.json

    user = {
        "username":username,
        "password":password.decode("utf-8"),
        "user_id":user_id.decode("utf-8")
    }
    # Change password and user_id data types from Byte into String

    new_user = users.get("users")
    new_user.append(user)
    # Take users attribute from users.json and put new data (user)
    # Users is list type

    users["users"] = new_user
    users = json.dumps(users, indent=4)
    # Convert users(dict types) into Json types

    with open("users.json", 'w') as f:
        f.write(users)
        # Write users to users.json file

def sign_in():
    while True:
        os.system("cls")
        # Clean terminal

        username = input("Input your username[minimum 4 Character]: ")
        if len(username) < 4:
            os.system("cls")
            # Clean terminal

            print("Please input username in 4 characters or more..\n")
            input("Enter to continue... ")
        else:
            break
    while True:
        os.system("cls")
        # Clean terminal

        password = getpass.getpass("Input your password[Minimum 8 Character]: ")
        # Take input for password form (hidden input)

        if len(password) < 8:
            os.system("cls")
            # Clean terminal

            print("Please input password in 8 characters or more..\n")
            input("Enter to continue...")
        else:
            confirm_password = getpass.getpass("Confirm password: ")
            # Take input for password form (hidden input)

            if password != confirm_password:
                os.system("cls")
                # Clean terminal

                print("Incorrect password or confirm password..please try again")
                input("Enter to continue... ")
                continue
            else:
                break

    add_user(username, password)
    # Add user into users.json logic 

    os.system("cls")
    print("Create account successfully....\n")
    input("Enter to continue... ")