import os
from . import database
import random

def play_game():
    while True:
        os.system("cls")
        print("Game Start!!!\n")
        print("1.Rock")
        print("2.Paper")
        print("3.Scissors")
        print("4.Exit from game")

        try:
            weapon_option = int(input("\nchoose your weapon(1-4): "))
            os.system("cls")
            if weapon_option >= 1 and weapon_option < 4:
                os.system("cls")
                enemy_weapon_option = random.randint(0, 2)
                weapon = database.option[weapon_option - 1]
                enemy_weapon = database.option[enemy_weapon_option]

                print(f"Your Weapon ->> {weapon}\n")
                print(f"Enemy Weapon ->> {enemy_weapon}")

                if weapon == enemy_weapon:
                    print("\nDraw!!")
                
                elif weapon == "Rock" and enemy_weapon == "Paper":
                    print("\nOh no You lose..")

                elif weapon == "Paper" and enemy_weapon == "Scissors":
                    print("\nOh no You lose..")

                elif weapon == "Scissors" and enemy_weapon == "Rock":
                    print("\nOh no You lose..")

                elif weapon == "Rock" and enemy_weapon == "Scissors":
                    print("\nYEAYY!! you winn..")

                elif weapon == "Paper" and enemy_weapon == "Rock":
                    print("\nYEAYY!! you winn..")

                elif weapon == "Scissors" and enemy_weapon == "Paper":
                    print("\nYEAYY!! you winn..")

                continue_option = input("\nContinue game? (y/n): ")

                if continue_option == 'n' or continue_option == 'N':
                    break
            
            elif weapon_option == 4:
                break

        except:
            os.system("cls")
            print("Please input on integer format")