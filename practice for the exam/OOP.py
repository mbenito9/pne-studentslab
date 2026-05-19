from pathlib import Path
import http.client
import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

class Seq:
    def __init__(self, body):
        self.lol = body
    def __str__(self):
        return self.lol
    def n_codons(self):
        length = len(self.lol)
        codons = length * 1/3
        return codons

class Gene(Seq):
    def __init__(self, lol, paco=""):
        super().__init__(lol)
        self.paco = paco
    def __str__(self):
        return self.paco
    def analyse(self):
        self.paco = str(self.lol) + "SEQGENE"
        lst = []
        for i in self.paco:
            lst.append(i)
        return lst

class Html:
    def __init__(self, endp):
        self.endp = endp
    def __str__(self):
        return self.endp
    def obtain_body(self):
        if self.endp == "/":
            body = Path("jv.html").read_text()
            type = "text/html"
            return body, type

port = 8080
ip = "localhost"

socketserver.TCPServer.allow_reuse_address = True

class Connection(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        analyse = urlparse(self.path)
        path = analyse.path
        arguments = parse_qs(analyse.query)

        body, type = Html("/").obtain_body()
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Content-Type", type)
        self.end_headers()

        self.wfile.write(body.encode())
        return
handler = Connection

with socketserver.TCPServer((ip, port), handler) as h:
    try:
        h.serve_forever()
    except KeyboardInterrupt:
        h.server_close()
if __name__ == "__main__":
    seq = Seq("hhwbhxkdhsx")
    print(seq)
    print(seq.n_codons())
    gene = Gene(seq)
    print(gene.analyse())





