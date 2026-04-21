import http.client

port = 8080
server = "localhost"

print(f"\nConnecting to server: {server}:{port}\n")

connection = http.client.HTTPConnection(server, port)

try:
    connection.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = connection.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

print(f"CONTENT: {data1}")