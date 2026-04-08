import http.server
import socketserver
from pathlib import Path

def get_file(base):
    folder = "html/info/"
    filename = folder + base + ".html"
    read = Path(filename).read_text()
    return read

port = 8080

socketserver.TCPServer.allow_reuse_address = True

class NewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        split = path.split("/")
        file = split[1]
        print(split)
        try:
            if file == "" or file == "index.html":
                c = Path("html/index.html").read_text()
            elif "info" in path:
                base = split[-1]
                base = base.strip(".html")
                c = get_file(base)
            else:
                f = path.find("/")
                filename = path[(f + 1):] + ".html"
                c = Path(filename).read_text()
            self.send_response(200)
        except FileNotFoundError:
            c = Path("html/error.html").read_text()
            self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(c.encode())))
        self.end_headers()
        self.wfile.write(c.encode())

handler = NewHandler

with socketserver.TCPServer(("localhost", port), handler) as httpd:
    print("Serving at port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()