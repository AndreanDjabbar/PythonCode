from data import continue_program
import os

def checking_Ip(ip):
    break_ip = ip.split('.')
    index_checking = 0

    if len(break_ip) == 4:
        while True:
            try:
                is_int = int(break_ip[index_checking])

                if is_int >= 0 and is_int < 256:
                    index_checking += 1
                    if index_checking == 4:
                        return True
                        
                
                else:
                    os.system("cls")
                    print("==== Minimum value is 0 and Maximum value is 255 ====\n")
                    continue_program()
                    return False

            except:
                os.system("cls")
                print("==== Its not integer..please input in integer format ====\n")
                continue_program()
                return False

    else:
        return False