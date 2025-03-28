import socket

# Crear TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Servidor TCP
host = 'localhost'  # Localhost
port = 5000         # Puerto
server = (host, port) 
sock.bind(server)
sock.listen(5)
print(f"Servidor escuchando en {host}:{port}")

try:
    while True:
        print('Esperando conexión')
        connection, client = sock.accept()
        print(f"Conexión establecida con {client}")

        while True:
            data = connection.recv(4096).decode()
            
            if not data:
                print('No hay datos', client)
                break

            print(f"Mensaje recibido: {data}")

            if data.upper() == "DESCONEXION":
                print("Cliente solicitó desconexión.")
                connection.close()
                print("Conexión cerrada.")
                break

            response = data.upper()
            message = response.replace("SERVIDOR", "CLIENTE")
            message_encode = message.encode()
            connection.sendall(message_encode)
        
except KeyboardInterrupt:
    print("Servidor detenido manualmente.")
finally:
    connection.close()
    print("Servidor cerrado")
