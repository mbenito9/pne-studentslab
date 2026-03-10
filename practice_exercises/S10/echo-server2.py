import socket

ip = "212.128.255.76"
port = 8080

listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to avoid the error 98
listening.bind((ip,port))
listening.listen()
print("The server is configured")

count = 0
while True:
    print("Waiting for clients to connect")

    try:
        (client_s, client_ip_port) = listening.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        listening.close()
        exit()
    else:
        count += 1
        print(f"CONNECTION {count}. Client ip,port: {client_ip_port}")
        #this sentence is shown when a client has connected
        message_raw = client_s.recv(2048)
        real_msg = message_raw.decode()
        print("Received message:", real_msg)

        client_s.send(f"ECHO: {real_msg}".encode())
        client_s.close()