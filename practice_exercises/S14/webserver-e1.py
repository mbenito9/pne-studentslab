import http.server
import socketserver

port = 8081

socketserver.TCPServer.allow_reuse_address = True

class NewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        split = path.split("/")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        if split[1] == "":
            c = "Welcome to my server"
        else:
            c = "Resource not available"
        self.send_header("Content-Length", str(len(c.encode())))
        self.end_headers()
        self.wfile.write(c.encode())
        return

handler = NewHandler

with socketserver.TCPServer(("localhost", port), handler) as httpd:
    print("Serving at port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()