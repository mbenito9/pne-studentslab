import http.server
import socketserver
from pathlib import Path

port = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)
        list_resource = self.path.split("?")
        print(list_resource)
        resource = list_resource[0]
        if resource == "/":
            response = 200
            c = Path("index.html").read_text()
            typ = "text/html"
        elif resource == "/listusers":
            response = 200
            c = Path("people-e1.json").read_text()
            typ = "application/json"
        else:
            response = 404
            c = Path("error.html").read_text()
            typ = "text/html"
        self.send_response(response)
        self.send_header("Content-Length:", str(len(str.encode(c))))
        self.send_header("Content-Type:", typ)
        self.end_headers()

        self.wfile.write(str.encode(c))
        return

handler = TestHandler

with socketserver.TCPServer(("", port), handler) as ht:
    print("Serving at port: ", port)
    try:
        ht.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        ht.server_close()
