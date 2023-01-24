from socket import *

serverPort = 2345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

print("[SERVER] Server is Starting...")

while True:
    serverSocket.listen()
    print("[SERVER] The Server is wait for Connection..")
    connection, clientAddress = serverSocket.accept()
    print("[SERVER] Got Connection from ", clientAddress)

    connected = True

    while connected:
        message_lenght = connection.recv(2048).decode()
        message_lenght = int(message_lenght)
        message = connection.recv(message_lenght).decode()
        if (message == "DC"):
            connected = False
        else:
            print(f"[{clientAddress}]", message)

        # send box
        connection.send(("Pesan diterima: "+message + "/n").encode())
    if (connected == False):
        print("[SERVER] Connection from "+str(clientAddress[0]) +
              ":" + str(clientAddress[1]) + 'is disconnected\n')

    connection.close()
