import os

def tutorial_game():
    cursor = 0
    step =["You will see 4 option while playing the game (1.Rock 2.Paper 3.Scissors 4.Exit from game) and you need choose one", 
            "option 1 - 3 is a weapon that you should choose and option 4 is for exit from the game",
            "Rule for win:\n\nYour Weapon - Enemy Weapon\n\nRock        - scissors\nPaper       - Rock\nScissors    - Paper\n",
            "explanation:\na. If your weapon is Rock and your enemy weapon is Scissors, you win the game (Rock > Scissors)\nb. If your weapon is same with your enemy weapon (example: rock with rock) its draw\nc. If your weapon is not on rule condition and not same weapon, you lose",
            "Enjoy The game!!..."]
    while True:
        os.system("cls")
        print(f"{step[cursor]}")

        if cursor == 0:
            print("\n1. Next")
            print("2. Exit")
            try:
                option = int(input("\n-> "))
                if option == 1:
                    cursor += 1
                elif option == 2:
                    break
                else:
                    os.system("cls")
                    print("The existed option is only 1")
            except:
                os.system("cls")
                print("Please input on integer format")

        elif cursor > 0 and cursor != 4:
            print("\n1. Next")
            print("2. Back")
            print("3. Exit")
            try:
                option = int(input("\n-> "))
                if option == 1:
                    cursor += 1
                elif option == 2:
                    cursor -= 1
                elif option == 3:
                    break
                else:
                    os.system("cls")
                    print("The existed option is only 1,2 or 3")
            except:
                os.system("cls")
                print("Please input on integer format")

        elif cursor == 4:
            continue_option = input("Finish with tutorial? (y/n): ")

            if continue_option == 'y' or continue_option == 'Y':
                break

            else:
                cursor = 0

