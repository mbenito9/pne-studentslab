import socketserver
from pathlib import Path
import http.server
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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
        elif path == "/get":
            genes = ["TTTGATCATAGTACTAG", "GTCATATAGAG", "CCCCTTTTG", "CCCCCCGGGA", "ATATCGCATCTCAGCTTC"]
            num_req = arguments["number"]
            num_req = int(num_req[0])
            seq = genes[num_req]
            dct = {"number": num_req, "seq": seq}
            c = read_html_file("get.html").render(new=dct)
        elif path == "/gene":
            gene_name = arguments["gene_name"]
            gene_name = gene_name[0]
            seq = Seq()
            file_name = gene_name + ".txt"
            seq.read_fasta(file_name)
            gene = {"gene_name": gene_name, "gene": seq}
            c = read_html_file("gene.html").render(gene=gene)
        elif path == "/opert":
            seq = arguments["msg"][0]
            opert = arguments["operation"][0]
            sequence = Seq(seq)
            if opert == "Rev":
                result = sequence.reverse()
            elif opert == "Info":
                result = sequence.info()
            elif opert == "Comp":
                result = sequence.complement()
            dct = {"seq": seq, "opert": opert, "result": result}
            c = read_html_file("operation.html").render(op=dct)

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