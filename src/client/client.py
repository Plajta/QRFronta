import socket
import sys

i = 1

while i:
    for line in sys.stdin:
        if line[0]=='p':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(("127.0.0.1", 9090))
            data = "Novej"
            clientSocket.send(data.encode())
            dataFromServer = clientSocket.recv(1024)
            print(dataFromServer.decode())
        elif line[0]=='o':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(("127.0.0.1", 9090))
            data = "Starej"
            clientSocket.send(data.encode())
            dataFromServer = clientSocket.recv(1024)
            print(dataFromServer.decode())
        elif line[0]=='d':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(("127.0.0.1", 9090))
            data = "Zadnej"
            clientSocket.send(data.encode())
            dataFromServer = clientSocket.recv(1024)
            print(dataFromServer.decode())
        if line[0]=='k' or line[0]=='':
            i = 0
            break