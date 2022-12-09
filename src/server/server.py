import requests
import socket
import uuid

# custom import
from database import redisbase

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9090

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print('Listening on port %s ...' % SERVER_PORT)

database = redisbase()

try:
    while True:    
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        dataFromClient = client_connection.recv(1024).decode()
        response = "OK"

        if dataFromClient == "Novej":
            UUID = uuid.uuid1()
            # print(str(len(lidi)+1)+", "+str(UUID))
            database.add(UUID, "pepa")
            response = str(UUID)
        elif dataFromClient == "Starej":
            retrieved = database.retrieve_all()
            if len(retrieved):
                database.set(retrieved[1:])
            response = str(UUID) + "    odebráno"
        elif dataFromClient  == "Zadnej":
            database.delete()

        print(database.retrieve_raw())

        # Send HTTP response
        #client_connection.sendall(response.encode()) tohle by se pak mohlo hodit
        client_connection.send(response.encode())
        client_connection.close()
except KeyboardInterrupt:
    print("End!")
    # Close socket
    server_socket.close()