from networks import receive_key_from_client

BUFFER_SIZE = 1024

if __name__ == "__main__":
    print("Iniciando servidor...")
    while True:
        data = receive_key_from_client(BUFFER_SIZE)
        print(f"Tecla recibida: {data.decode()}")
