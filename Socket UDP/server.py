import socket

x = socket.socket()
host = socket.gethostname()
port = 8080
x.bind((host, port))
x.listen(1)

print("Server Sedang Berjalan....")
conn, addr = x.accept()
print("Dapat koneksi dari", addr)
conn.send("Terima Kasih telah menghubungi server".encode())
while 1:
    message = input("Masukkan pesan: ")
    message = str(message).encode()
    conn.send(message)
    print("pesan terkirim...")
    recv = conn.recv(2046)
    print("Pesan dari client: ", recv.decode())
