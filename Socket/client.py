import socket

my_socket = socket.socket()

host = '127.0.0.3'
port = 20111
my_socket.connect((host,port))

while True:
    msg = input("input here")
    if msg == 'q':
        break
    my_socket.send(msg.encode())
    rec = my_socket.recv(1024).decode()
    print("response : ",rec)
my_socket.close()