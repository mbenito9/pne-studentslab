import socket

IP = "212.128.255.64"
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("HELLOOO"))
s.close()