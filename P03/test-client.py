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

