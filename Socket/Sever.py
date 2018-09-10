import socket

my_socket = socket.socket()


host = '127.0.0.3' # Local Host
port = 20111 # Create Port Value > 10000   ->  Because Your Device Have Ports Else And Its Value Maybe <= 10000

my_socket.bind((host,port))

my_socket.listen(3)

conn,add = my_socket.accept()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Got The Equation : ",data)
    try:
        res = str(eval(data))
        print("The Result Is",res)
    except:
        print("not valid equation")
    conn.send(res.encode())
conn.close()