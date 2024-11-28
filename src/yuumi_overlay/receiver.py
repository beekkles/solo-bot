import requests
import json
import time
source_url = "http://192.168.1.35:5000"
save_path = "data.json"


def fetch_and_save_json():
    try:
        response = requests.get(source_url)
        response.raise_for_status()

        data = response.json()

        with open(save_path, 'w') as file:
            json.dump(data, file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con {source_url}: {e}")
    except json.JSONDecodeError:
        print("JSON invñalido.")
    except Exception as e:
        print(f"Error: {e}")

def fetch_loop():
    while True:
        fetch_and_save_json()
        time.sleep(1)

if __name__ == "__main__":
    fetch_loop()