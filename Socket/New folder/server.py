import socket

s1  = socket.socket()

host = '127.0.0.2'
port = 20001

s1.bind((host,port))
s1.listen(1)
conn,add = s1.accept()

data = conn.recv(1024).decode()
res = str(eval(data))
print("result is : ",res)
s1.close()