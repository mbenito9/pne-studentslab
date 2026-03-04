import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.128.255.76" # depends on the computer the server is running

flag = True
while flag:
    message = str(input("Enter your requested message"))
    if message != "STOP":

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(str.encode(message))
        s.close()
    else:
        flag = False