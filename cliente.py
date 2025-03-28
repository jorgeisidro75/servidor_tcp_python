import socket

# Crear TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar con socket del servidor
host = 'localhost'
port = 5000
server_address = (host, port)
sock.connect(server_address)

try:

    #Enviar mensaje
    while True:
        message = input("Ingrese un mensaje: ")
        sock.sendall(message.encode())
        print(message)

        if message.upper() == "DESCONEXION":
            print("Cerrando conexión...")
            #sock.close() 
            break

        response = sock.recv(4096).decode()
        
        print(f"Respuesta del servidor: {response}")


finally:
    sock.close()
    print('Conexión cerrada')
