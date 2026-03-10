import socket

ip = "212.128.255.76"
port = 8080

listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to avoid the error 98
listening.bind((ip,port))
listening.listen()
print("The server is configured")

while True:
    print("Waiting for clients to connect")

    try:
        (client_s, client_ip_port) = listening.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        listening.close()
        exit()
    else:
        print("A client has connected to the server")
        #this sentence is shown when a client has connected
        message_raw = client_s.recv(2048)
        real_msg = message_raw.decode()
        print("received:", real_msg)

        client_s.send("Hello, I am the Happy Server\n".encode())
        client_s.close()