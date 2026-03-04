from Client0 import Client

port = 8080
ip = "212.128.255.76"

print("-----| Practice 2, Exercise 3 |------")
c = Client(ip,port)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
