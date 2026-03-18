from pathlib import Path
import socket
import termcolor

ip = "127.0.0.1"
port = 8080

def get_file(base):
    folder = "html/info/"
    filename = folder + base + ".html"
    read = Path(filename).read_text()
    return read

def talking_client(s):
    msg_raw = s.recv(2000)
    msg = msg_raw.decode()
    print("message from the client")

    lines = msg.split("\n")
    req_line = lines[0]
    split = req_line.split(" ")
    path = split[1]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")
    if path == "/info/A" or path == "/info/C" or path == "/info/T" or path == "/info/G":
        b = path.split("/")
        body = get_file(b[2]) + "\n"
    else:
        filename = "html/" + "error.html"
        body = Path(filename).read_text() + "\n"
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((ip,port))
ls.listen()
print("ECHO server created")

while True:
    print("Waiting for clients...")
    try:
        (cs, c_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped")
        ls.close()
        exit()
    else:
        talking_client(cs)
        cs.close()