import json
import time
import tkinter as tk
from pynput import keyboard

q_cd = 6.5
e_cd = 10

file_path = 'data.json'
last_used = {'q': 0, 'w': 0, 'e': 0}
cooldowns = {'q': 0, 'e': 0}
last_ability_haste = None

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
    return None

def get_ability_haste(data):
    try:
        return data['championStats']['abilityHaste']
    except KeyError:
        print("Key 'abilityHaste' not found in the JSON data.")
        return None

def calculate_ability_haste():
    global last_ability_haste
    data = read_json(file_path)
    if data:
        ability_haste = get_ability_haste(data)
        if ability_haste is not None:
            last_ability_haste = ability_haste
            return ability_haste
    return last_ability_haste

class AbilityOverlay:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove titlebar
        self.root.config(bg='magenta')  # Set a color to be transparent
        self.root.attributes('-transparentcolor', 'magenta')
        self.root.geometry(f'+100+100')  # Adjust x and y as needed

        self.q_label = tk.Label(root, text="Q: Ready", font=("Helvetica", 16), bg='magenta')
        self.q_label.place(x=10, y=10)
        self.e_label = tk.Label(root, text="E: Ready", font=("Helvetica", 16), bg='magenta')
        self.e_label.place(x=110, y=10)

        self.ability_haste = calculate_ability_haste()
        self.last_used = {'q': 0, 'e': 0}

        self.pressed_keys = set()
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

        self.update_labels()
        self.update_ability_haste()

    def update_labels(self):
        current_time = time.time()
        if self.ability_haste is not None:
            q_ah = q_cd / (1 + self.ability_haste / 100)
            e_ah = e_cd / (1 + self.ability_haste / 100)

            if current_time - self.last_used['q'] < q_ah:
                self.q_label.config(text=f"Q: {q_ah - (current_time - self.last_used['q']):.2f}s")
            else:
                self.q_label.config(text="Q: Ready")

            if current_time - self.last_used['e'] < e_ah:
                self.e_label.config(text=f"E: {e_ah - (current_time - self.last_used['e']):.2f}s")
            else:
                self.e_label.config(text="E: Ready")

        self.root.after(100, self.update_labels)

    def update_ability_haste(self):
        self.ability_haste = calculate_ability_haste()
        self.root.after(10000, self.update_ability_haste)

    def on_press(self, key):
        try:
            if key.char in ['q', 'e']:
                self.pressed_keys.add(key.char)
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key.char in self.pressed_keys:
                current_time = time.time()
                if self.ability_haste is not None:
                    q_ah = q_cd / (1 + self.ability_haste / 100)
                    e_ah = e_cd / (1 + self.ability_haste / 100)

                    if key.char == 'q' and current_time - self.last_used['q'] >= q_ah:
                        self.last_used['q'] = current_time
                    elif key.char == 'e' and current_time - self.last_used['e'] >= e_ah:
                        self.last_used['e'] = current_time
                self.pressed_keys.remove(key.char)
        except AttributeError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AbilityOverlay(root)
    root.mainloop()