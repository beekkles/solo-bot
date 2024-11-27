from networks import send_key_to_server

if __name__ == "__main__":
    print("Iniciando cliente...")
    while True:
        tecla = input("Presiona una tecla para enviar: ")
        send_key_to_server(tecla)
