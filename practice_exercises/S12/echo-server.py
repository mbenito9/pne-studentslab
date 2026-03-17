import socket
import termcolor

ip = "127.0.0.1"
port = 8080

def talking(s):
    msg_raw = s.recv(2000)
    msg = msg_raw.decode()
    print("Message from the client:")
    termcolor.cprint(msg, "green")

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()

print("Echo server configured")

while True:
    print("Waiting for clients...")
    try:
        (client_s, c_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped")
        ls.close()
        exit()
    else:
        talking(client_s)
        client_s.close()