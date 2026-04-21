import socketserver
import http.server
from pathlib import Path

port = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        list_resource = self.path.split('?')
        resource = list_resource[0]
        if resource == "/":
            c = Path("index.html").read_text()
            c_type = "text/html"
            error_code = 200
        elif resource == "/listusers":
            c = Path("people-3.json").read_text()
            c_type = "application/json"
            error_code = 200
        else:
            c = Path("error.html").read_text()
            c_type = "text/html"
            error_code = 404

        self.send_response(error_code)
        self.send_header("Content-Type", c_type)
        self.send_header("Content-Length", str(len(str.encode(c))))
        self.end_headers()
        self.wfile.write(str.encode(c))
        return

Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Serving at port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()