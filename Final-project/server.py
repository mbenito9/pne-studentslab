import http.server
import http.client
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
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
        analyse_path = urlparse(self.path)
        path = analyse_path.path
        arg = parse_qs(analyse_path.query)
        body = ""
        try:
            self.send_response(200)
            if path == "/":
                body = Path("html/main_page.html").read_text()

            elif path == "/listSpecies":
                server = "rest.ensembl.org"
                endp = "/info/species"
                params = "?content-type=application/json"
                url = server + endp + params

                conn = http.client.HTTPConnection(server)
                conn.request("GET", endp + params)
                ans = conn.getresponse()

                dict_data = json.loads(ans.read().decode())
                lst_species = dict_data["species"]
                total = 0
                if "limitval" in arg.keys():
                    limit = int(arg["limitval"][0])
                else:
                    limit = 0
                req_species = """
                <ul>\n
                """
                for specie in lst_species:
                    name = specie["display_name"]
                    req_species += f"<li>{name}</li>\n"
                    total += 1
                    if total == limit:
                        break
                req_species += "</ul>"
                dct = {"limit": limit, "total_species": len(lst_species), "names": req_species}
                body = read_html_file("basic1.html").render(changes=dct)

            elif path == "/karyotype" or path == "/chromosomeLength":
                specie = arg["species"][0]
                specie_new = specie.replace(" ", "%20")
                server = "rest.ensembl.org"
                endp = f"/info/assembly/{specie_new}"
                params = "?content-type=application/json"

                conn = http.client.HTTPConnection(server)
                conn.request("GET", endp + params)
                ans = conn.getresponse()

                dict_data = json.loads(ans.read().decode())
                if path == "/karyotype":
                    karyo_lst = dict_data["karyotype"]
                    total_chr = """
                    <ul>\n
                    """
                    for karyo in karyo_lst:
                        total_chr += f"<li>{karyo}</li>\n"
                    total_chr += "</ul>"

                    dct = {"chroms": total_chr, "specie": specie}
                    body = read_html_file("basic2.html").render(changes=dct)
                elif path == "/chromosomeLength":
                    n_chr = arg["chromo"][0]
                    lst_region = dict_data["top_level_region"]
                    for chromosome in lst_region:
                        if chromosome["name"] == n_chr:
                            length = chromosome["length"]
                    dct = {"number": n_chr, "len": length}
                    body = read_html_file("basic3.html").render(changes=dct)

            elif path == "/geneLookup" or path == "/geneSeq":
                gene_name = arg["gene"][0]
                server = "rest.ensembl.org"
                endp = f"/lookup/symbol/homo_sapiens/{gene_name}"
                params = "?content-type=application/json"

                conn = http.client.HTTPConnection(server)
                conn.request("GET", endp + params)
                ans = conn.getresponse()

                dict_data = json.loads(ans.read().decode())
                iden = dict_data["id"]
                dct = {"id": iden, "gene": gene_name}

                if path == "/geneLookup":
                    body = read_html_file("medium_id.html").render(changes=dct)
                if path == "/geneSeq":
                    server = "rest.ensembl.org"
                    endp = f"/sequence/id/{iden}"
                    params = "?content-type=application/json"

                    conn = http.client.HTTPConnection(server)
                    conn.request("GET", endp + params)
                    ans = conn.getresponse()
                    dict_data = json.loads(ans.read().decode())
                    dct["sequence"] = dict_data["seq"]
                    body = read_html_file("medium_seq.html").render(changes=dct)

        except Exception:
            self.send_response(404)
            body = Path("html/error.html").read_text()
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body.encode())))
        self.end_headers()
        self.wfile.write(body.encode())
        return

handler = TestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()