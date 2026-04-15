import socketserver
import http.server
from urllib.parse import parse_qs, urlparse
from pathlib import Path

port = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        self.send_response(200)
        if  path == "/":
            c = Path("html/form-e2.html").read_text()
        elif path == "/echo":
            body = """
            <!DOCTYPE html>
            <html lang="en" dir="ltr">
                <head>
                    <meta charset="utf-8">
                    <title>received message</title>
                </head>
                <body>
                    <h1>RECEIVED MESSAGE: </h1>
            """
            lst = arguments["msg"]
            msg = lst[0]
            for key, value in arguments.items():
                if key == "chk":
                    msg = msg.upper()
            body += f"""
                    <p>{msg}</p>
                    <p></p>
                    <a href="http://127.0.0.1:8080/">Main Page</a>
                </body>
            </html>
            """
            c = "\n" + body
        else:
            c = Path("html/error.html").read_text()
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(c.encode())))
        self.end_headers()
        self.wfile.write(str.encode(c))
        return

Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as lol:
    print("Sering at port:", port)
    try:
        lol.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        lol.server_close()