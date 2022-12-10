import requests
import socket
import uuid
import base64
import sys

# custom import
from database import RedisBase

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9090


# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print('Listening on port %s ...' % SERVER_PORT)

database = RedisBase()


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


def isUUID(s):
    try:
        uuid.UUID(s)
        return True
    except Exception:
        return False


while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    dataFromClient = client_connection.recv(1024).decode()
    response = "OK"

    if dataFromClient.count(";") == 1:
        command = dataFromClient.split(";")
        if command[0] == "new-user":
            if isBase64(command[1].encode("ascii")):
                UUID = uuid.uuid1()
                database.add(UUID, command[1])
                response = str(UUID)
        elif command[0] == "remove-user":
            if command[1] == "all":
                database.delete_all()
                response = "removed;all"
            elif isUUID(command[1]):
                database.delete(command[1])
                response = "removed;" + command[1]
        elif command[0] == "check-pos":
            if isUUID(command[1]):
                response = database.check(uuid.UUID(command[1]))[0]+";"+database.check(uuid.UUID(command[1]))[1]

    print(dataFromClient)
    # Send HTTP response
    # client_connection.sendall(response.encode()) tohle by se pak mohlo hodit
    client_connection.send(response.encode())
    client_connection.close()
print("End!")
# Close socket
server_socket.close()
