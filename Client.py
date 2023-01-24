from socket import *

serverName = 'localhost'
serverPort = 2345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def send(msg):
    message = msg.encode()
    message_length = len(message)
    send_length = str(message_length).encode()
    clientSocket.send(send_length)
    clientSocket.send(message)


x = int(input('Jumlah anggota kelompok: '))
for i in range(x):
    message = input('Masukkan Pesan: <Nama(spasi)NIM ==>')

    send(message)

    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())
    if (i == x-1):
        send('DC')
clientSocket.close()
