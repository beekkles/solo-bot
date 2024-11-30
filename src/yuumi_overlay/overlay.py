import threading
import tkinter as tk
from haste import AbilityOverlay
from receiver import fetch_loop

def start_receiver():
    fetch_loop()

if __name__ == "__main__":
    receiver_thread = threading.Thread(target=start_receiver)
    receiver_thread.daemon = True
    receiver_thread.start()

    root = tk.Tk()
    app = AbilityOverlay(root)
    root.mainloop()