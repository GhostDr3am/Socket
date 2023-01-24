import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host, port))
print("Terhubung ke server")
message = s.recv(1024)
message = message.decode()
print("Pesan dari server: ", message)
while 1:
    message = s.recv(2048)
    message = message.decode()
    print("Pesan dari server: ", message)
    new_message = input("Masukkan pesan: ")
    new_message = str(new_message).encode()
    s.send(new_message)
    print("pesan terkirim...")
    message = s.recv(2048)
    message = message.decode()
