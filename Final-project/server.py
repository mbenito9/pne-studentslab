import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse

port = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        analyse_path = urlparse(self.path)
        path = analyse_path.path
        arg = parse_qs(analyse_path.query)

        if path == "/":
            body = Path("html/main_page.html").read_text()

