import socket
import keyboard
import pyautogui

receiver_ip = '127.0.0.1'
port = 25565

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_key(key):
    #UDP
    client.sendto(key.encode(), (receiver_ip, port))

keyboard.on_press(lambda e: send_key(e.name))

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((receiver_ip, port))

while True:
    data, _ = server.recvfrom(1024)
    pyautogui.press(data.decode())
