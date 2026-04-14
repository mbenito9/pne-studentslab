import http.server
import socketserver
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
            c = Path("html/form-e1.html").read_text()
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
            for key, value in arguments.items():
                if key == "msg":
                    body += f"""
                            <p>{value[0]}</p>
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

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Serving at port:", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()