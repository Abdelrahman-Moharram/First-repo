import socket 
s1 = socket.socket()
host = '127.0.0.2'
port = 20001
s1.connect((host,port))

element = input()
s1.send(element.encode())
res = s1.recv(1024).decode()
print("The Result Is  ",res,'\n')
s1.close()