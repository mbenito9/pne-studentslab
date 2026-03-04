from Client0 import Client

practice = 2
ex = 1
print(f"-----| Practice {practice}, Exercise {ex} |------")

port = 8080
ip = "212.128.255.76"

c = Client(ip, port)
c.ping()