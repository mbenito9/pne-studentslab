import http.server
import http.client
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import jinja2 as j

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
        if path == "/":
            self.send_response(200)
            body = Path("html/main_page.html").read_text()
        elif path == "/listSpecies":
            self.send_response(200)
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
                name = specie["common_name"]
                req_species += f"<li>{name}</li>\n"
                total += 1
                if total == limit:
                    break
            req_species += "</ul>"
            dct = {"limit": limit, "total_species": len(lst_species), "names": req_species}
            body = read_html_file("basic1.html").render(changes=dct)
        elif path == "/karyotype":
            self.send_response(200)
            server = "rest.ensembl.org"
            specie = arg["specie"]
            endp = f"/info/assembly/{specie}"
            params = "?content-type=application/json"
            url = server + endp + params

            conn = http.client.HTTPConnection(server)
            conn.request("GET", endp + params)
            ans = conn.getresponse()

            dict_data = json.loads(ans.read().decode())
            karyo_lst = dict_data["karyotype"]
            total_chr = """
            <ul>\n
            """
            for karyo in karyo_lst:
                total_chr += f"<li>{karyo}</li>\n"
            total_chr += "</ul>"
            dct = {"chroms": total_chr}
            body = read_html_file("basic1.html").render(changes=dct)
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
