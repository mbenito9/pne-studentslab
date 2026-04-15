import socketserver
from pathlib import Path
import http.server
from urllib.parse import parse_qs, urlparse

port = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        self.send_response(200)
        if path == "/":
            c = Path("html/index.html").read_text()
        elif path == "/ping":
            c = Path("html/ping.html").read_text()
        else:
            c = Path("html/error.html").read_text()
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(c.encode())))
        self.end_headers()
        self.wfile.write(str.encode(c))
        return

Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Serving at port:", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()