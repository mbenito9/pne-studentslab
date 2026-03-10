import socket
from Client0 import Client

ip = "212.128.255.76"
port = 8080

client = Client(ip,port)
for i in range(5):
    s = f"Message {i}"
    print(f"To the server: {s}")
    message = client.talk(str(s))
    print(f"From the Sever: {message}\n")