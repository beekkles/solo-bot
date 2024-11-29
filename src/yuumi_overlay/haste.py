import json

q_cd = 6.5
w_cd = 0
e_cd = 10
r_cd = [120, 110, 100]

file_path = 'data.json'

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_ability_haste(data):
    try:
        return data['championStats']['abilityHaste']
    except KeyError:
        print("Key 'abilityHaste' not found in the JSON data.")
        return None

def get_yuumi_r_level(data):
    try:
        return data['abilities']['R']['abilityLevel']
    except KeyError:
        print("Key 'abilityLevel' for YuumiQ not found in the JSON data.")
        return None

def calculate_ability_haste():
    data = read_json(file_path)
    if data:
        ability_haste = get_ability_haste(data)
        r_level = get_yuumi_r_level(data)
        if ability_haste is not None and r_level is not None:
            q_ah = q_cd / (1 + ability_haste / 100)
            w_ah = w_cd / (1 + ability_haste / 100)
            e_ah = e_cd / (1 + ability_haste / 100)
            r_ah = r_cd[r_level - 1] / (1 + ability_haste / 100)
            return q_ah, w_ah, e_ah, r_ah
    return None, None, None, None