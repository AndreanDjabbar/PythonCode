import os
import json

def create_file():
    try:
        with open("history.json", 'r') as file:
            file.read()
    except:
        data_dict = {
            "Results":[]
        }
        data_json = json.dumps(data_dict, indent=4)
        with open("history.json", 'w', encoding="utf-8") as file:
            file.write(data_json)

def read_file():
    with open("history.json", 'r') as file:
        data_dict = json.load(file)
    return data_dict

def create_history(result:str, played_time:str):
    data_dict_results = read_file()
    results = data_dict_results.get("Results")
    data_dict = {
        "Result":result,
        "Played Time":played_time
    }
    results.append(data_dict)
    data_json = json.dumps(data_dict_results, indent=4)
    with open("history.json", 'w', encoding="utf-8") as file:
        file.write(data_json)

def history():
    os.system("cls")
    try:
        data_dict = read_file()
    except:
        print("No History..")
    results = data_dict.get("Results")
    for index, data in enumerate(results):
        print(f"Game {index+1}: ")
        result = data.get("Result")
        played_time = data.get("Played Time")
        print(f"Result      : {result}")
        print(f"Played Time : {played_time}\n")
    input("\nEnter to Continue... ")