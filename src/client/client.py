import socket
import sys
import base64
import uuid

i = 1
uid = 0


def isUUID(s):
    try:
        uuid.UUID(s)
        return True
    except Exception:
        return False


while i:
    for line in sys.stdin:
        splitinput = line.split()
        if splitinput[0] == 'add':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(("127.0.0.1", 9090))
            name = line[len(splitinput[0])+1:]
            try:
                data = "new-user;" + base64.b64encode(name.encode("ascii")).decode("ascii")
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                uid = uuid.UUID(dataFromServer.decode())
                print(uid)
            except UnicodeError as E:
                print(E)

        elif splitinput[0] == 'remove' and len(splitinput) == 2:
            if splitinput[1] == "last":
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect(("127.0.0.1", 9090))
                data = "remove-user;" + str(uid)
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                print(dataFromServer.decode())

            elif splitinput[1] == "all":
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect(("127.0.0.1", 9090))
                data = "remove-user;all"
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                print(dataFromServer.decode())

            elif splitinput[1]:
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect(("127.0.0.1", 9090))
                data = "remove-user;" + splitinput[1]
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                output = dataFromServer.decode()
                print(f"UUID/Index {splitinput[1]} does not exist" if output == "None" else output)

        elif splitinput[0] == 'check':
            if len(splitinput) == 1:
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect(("127.0.0.1", 9090))
                data = "check-pos;" + str(uid)
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                print(dataFromServer.decode())

            elif len(splitinput) == 2 and isUUID(splitinput[1]):
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect(("127.0.0.1", 9090))
                data = "check-pos;" + splitinput[1]
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                print(dataFromServer.decode())

        elif splitinput[0] == 'move' and len(splitinput) == 3:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(("127.0.0.1", 9090))
            data = "move-back;" + splitinput[1] + ";" + splitinput[2]
            clientSocket.send(data.encode())
            dataFromServer = clientSocket.recv(1024)
            print(dataFromServer.decode())


        if splitinput[0] == 'k' or splitinput[0] == '':
            i = 0
            break
