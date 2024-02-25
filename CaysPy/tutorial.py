import os

def guides():
    guides = {
        1:"Welcome to CaysPy Game!",
        2:"You have an important mission to find a secret treasure among 4 caves",
        3:"You can only choose one cave",
        4:"If you get a right cave, you got a treasure and win the game",
        5:"Otherwise, if you get a wrong cave, you lose",
        6:"Enjoy the game!!"
    }
    return guides

def tutorial():
    is_loop = True
    pages = guides()
    page = 1
    while is_loop == True:
        os.system("cls")
        print(pages.get(page))
        if page == 1:
            print("\n1. Next")
            print("2. Exit")
            try:
                page_option = int(input("Choose: "))
                if page_option < 1 or page_option > 2:
                    os.system("cls")
                    print("Please input within range [1-2] !")
                    input("Enter to continue.. ")
            except:
                os.system("cls")
                print("Please input on integer format")
                input("Enter to continue.. ")
            if page_option == 1:
                page +=1
            elif page_option == 2:
                is_loop = False
        
        elif page == len(pages):
            print("\n1. Previous")
            print("2. Exit")
            try:
                page_option = int(input("Choose: "))
                if page_option < 1 or page_option > 2:
                    os.system("cls")
                    print("Please input within range [1-2] !")
                    input("Enter to continue.. ")
            except:
                os.system("cls")
                print("Please input on integer format")
                input("Enter to continue.. ")
            if page_option == 1:
                page -=1
            elif page_option == 2:
                is_loop = False
        
        else:
            print("\n1. Previous")
            print("2. Next")
            print("3. Exit")
            try:
                page_option = int(input("Choose: "))
                if page_option < 1 or page_option > 2:
                    os.system("cls")
                    print("Please input within range [1-3] !")
                    input("Enter to continue.. ")
            except:
                os.system("cls")
                print("Please input on integer format")
                input("Enter to continue.. ")
            if page_option == 1:
                page -=1
            elif page_option == 2:
                page += 1
            elif page_option == 3:
                is_loop = False