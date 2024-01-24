import os
import getpass
from base import main_page, secret_key, generate_users
from cryptography.fernet import Fernet as fr

def checking_user(username:str, password:str) -> bool:
    fernet = fr(secret_key)
    user_id = username + password
    users = generate_users()
    users = users.get("users")
    
    for user in users:
        current_user = user.get("user_id").encode("utf-8")
        # Encode user_id in users.json from String type into Bytes
        decoded_user = fernet.decrypt(current_user).decode("utf-8")
        # Decrypt current_user and decode from Bytes into String type
        if decoded_user == user_id:
            return True
    return False
    # Check user is exist in users.json or not
    # If exist, it will return True. Otherwise return False

def login():
    os.system("cls")
    # Clean terminal

    username = input("Input your username: ")
    password = getpass.getpass("Input your password: ")
    # Take input for password form (hidden input)
    is_exist = checking_user(username, password)
    
    if is_exist == True:
        main_page(username)
    else:
        os.system("cls")
        # Clean terminal

        print("User is not Exist.. please check your Username and Password..\n")
        input("Enter to Continue.. ")

