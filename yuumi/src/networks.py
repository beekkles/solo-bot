import socket
from shared.config import YUUMI_IP, YUUMI_PORT

def receive_key_from_client(buffer_size):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((YUUMI_IP, YUUMI_PORT))
        print(f"Servidor escuchando en {YUUMI_IP}:{YUUMI_PORT}")

        data, addr = sock.recvfrom(buffer_size)
        print(f"Mensaje recibido de {addr}: {data.decode()}")

        return data
