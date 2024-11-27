import socket
from shared.config import YUUMI_IP, YUUMI_PORT

def send_key_to_server(data):
    """
    Envía un mensaje al servidor.
    data: Los datos que queremos enviar (cadena de texto).
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(data.encode(), (YUUMI_IP, YUUMI_PORT))
        print(f"Mensaje enviado a {YUUMI_IP}:{YUUMI_PORT}: {data}")
