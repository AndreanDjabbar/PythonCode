import random
import os
from datetime import datetime
from history import create_history

def caves():
    os.system("cls")
    print(
            """
    Cave 1  Cave 2  Cave 3  Cave 4 
    ______  ______  ______  ______
    |    |  |    |  |    |  |    |
    |    |  |    |  |    |  |    |
    
"""
        )

def cave_validation(cave_option:int):
    os.system("cls")
    rand_cave = random.randint(1, 4)
    match(rand_cave):
        case 1:
            print(
            """
    Cave 1  Cave 2  Cave 3  Cave 4 
    ______  ______  ______  ______
    |    |  |    |  |    |  |    |
    | $  |  | x  |  | x  |  |  x |
    
"""
        )
        case 2:
            print(
            """
    Cave 1  Cave 2  Cave 3  Cave 4 
    ______  ______  ______  ______
    |    |  |    |  |    |  |    |
    | x  |  | $  |  | x  |  |  x |
    
"""
        )
        case 3:
            print(
            """
    Cave 1  Cave 2  Cave 3  Cave 4 
    ______  ______  ______  ______
    |    |  |    |  |    |  |    |
    | x  |  | x  |  | $  |  |  x |
    
"""
        )
        case 4:
            print(
            """
    Cave 1  Cave 2  Cave 3  Cave 4 
    ______  ______  ______  ______
    |    |  |    |  |    |  |    |
    | x  |  | x  |  | x  |  |  $ |
    
"""
        )
    result = ""
    if cave_option == rand_cave:
        print("\nCONRATULATIONS!! You got the correct cave !")
        result = "Win"
    else:
        print("\nOh No !! that is a wrong cave..")
        result = "Lose"
    played_time = str(datetime.now())
    create_history(result, played_time)
    input("Enter to Continue.. ")

def play():
    is_loop = True
    while is_loop == True:
        caves()
        try:
            cave_option = int(input("Choose one cave[1-4]: "))
        except:
            os.system("cls")
            print("Please input on integer format and within range [1-4] !")
            input("Enter to continue.. ")
        if cave_option < 1 or cave_option > 4:
            os.system("cls")
            print("Please input within range [1-4] !")
            input("Enter to continue.. ")
        else:
            cave_validation(cave_option)
            is_loop = False
