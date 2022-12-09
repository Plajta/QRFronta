import requests
import socket

# custom import
from database import *

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9090

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    dataFromClient = client_connection.recv(1024).decode()
    print(dataFromClient)

    # Send HTTP response
    response = "Cool"
    #client_connection.sendall(response.encode()) tohle by se pak mohlo hodit
    client_connection.send(response.encode())
    client_connection.close()

# Close socket
server_socket.close()