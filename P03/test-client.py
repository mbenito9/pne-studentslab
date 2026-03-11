import socket
from Client0 import Client

ip = "127.0.0.1"
port = 8080

client = Client(ip,port)
commnds = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
for i in commnds:
    print(f" * TESTING {i}...")
    if i == "PING":
        ans = client.talk(i)
        print(ans)
    elif i == "GET":
        seq = client.talk(i + " 0")
        print(seq)
    elif i == "INFO":
        ans = client.talk(i + f" {seq}")
        print(ans)

