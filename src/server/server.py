import socket
import uuid

# custom imports
from database import RedisBase
from misc import *

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

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    dataFromClient = client_connection.recv(1024).decode()
    response = "OK"
    command = dataFromClient.split(";")
    if len(command) == 2:
        if command[0] == "new-user":
            if isBase64(command[1].encode("ascii")):
                UUID = uuid.uuid1()
                database.add(UUID, command[1])
                response = str(UUID)
        elif command[0] == "remove-user":
            if command[1] == "all":
                database.delete_all()
                response = "removed;all"
            else:
                response = "removed" if database.delete(command[1]) else str(None)
        elif command[0] == "check-pos":
            response = str(database.find(command[1])[0])+";"+str(database.find(command[1])[1])
    elif len(command) == 3:
        if command[0] == "move-back" and isUUID(command[1]) and isInt(command[2]):
            oldindex = database.find(command[1])[0]
            database.move(oldindex, abs(int(command[2]))+oldindex)

    print(dataFromClient)
    print(response)
    #print(database.retrieve_raw())
    # Send HTTP response
    # client_connection.sendall(response.encode()) tohle by se pak mohlo hodit
    client_connection.send(response.encode())
    client_connection.close()
# Close socket
server_socket.close()
