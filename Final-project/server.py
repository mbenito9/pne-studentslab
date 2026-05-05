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

def get_json_data(endp, add):
    server = "rest.ensembl.org"
    params = "?content-type=application/json"

    if len(add) != 0:
        params += add

    conn = http.client.HTTPConnection(server)
    conn.request("GET", endp + params)
    ans = conn.getresponse()

    dict_data = json.loads(ans.read().decode())
    return dict_data


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
                dict_data = get_json_data("/info/species", "")
                lst_species = dict_data["species"]
                total = 0
                json = arg["json"][0]

                if "limitval" in arg.keys():
                    limit = int(arg["limitval"][0])
                else:
                    limit = 0

                name_lst = []
                for specie in lst_species:
                    name = specie["display_name"]
                    name_lst.append(name)
                    total += 1
                    if total == limit:
                        break

                dct = {"limit": limit, "total_species": len(lst_species), "names": req_species}
                if json == "1":
                    c_type = "application/json"
                    dct["names"] = name_lst

                else:
                    req_species = """
                    <ul>\n
                    """
                    for name in name_lst:
                        req_species += f"<li>{name}</li>\n"
                    req_species += "</ul>"
                    body = read_html_file("basic1.html").render(changes=dct)
                    c_type = "text/html"

            elif path == "/karyotype" or path == "/chromosomeLength":
                specie = arg["species"][0]
                specie_new = specie.replace(" ", "%20")

                dict_data = get_json_data(f"/info/assembly/{specie_new}", "")
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

            elif path == "/geneLookup" or path == "/geneSeq" or path == "/geneInfo" or path == "/geneCalc":
                gene_name = arg["gene"][0]
                dict_data = get_json_data(f"/lookup/symbol/homo_sapiens/{gene_name}", "")
                iden = dict_data["id"]
                dct = {"id": iden, "gene": gene_name}

                if path == "/geneLookup":
                    body = read_html_file("medium_id.html").render(changes=dct)

                if path == "/geneSeq" or path == "/geneCalc":
                    dict_data = get_json_data(f"/sequence/id/{iden}", "")
                    seq = dict_data["seq"]

                    if path == "/geneCalc":
                        object_seq = Seq(seq)

                        info_str = str(object_seq.info())
                        i = info_str.index("Most")
                        strp_info = info_str[:i]

                        dct["info"] = strp_info
                        body = read_html_file("medium_calc.html").render(changes=dct)

                    if path == "/geneSeq":
                        dct["sequence"] = seq
                        body = read_html_file("medium_seq.html").render(changes=dct)

                if path == "/geneInfo":
                    start = dict_data["start"]
                    end = dict_data["end"]
                    length = int(end) - int(start)
                    add = {"start": start, "end": end, "len": length, "chr": dict_data["seq_region_name"]}
                    new = dct | add
                    body = read_html_file("medium_Info.html").render(changes=new)
            elif path == "/geneList":
                chr = arg["chromo"][0]
                st = arg["start"][0]
                end = arg["end"][0]
                lst_data = get_json_data(f"/overlap/region/human/{chr}:{st}-{end}", ";feature=gene")

                id_lst = []
                for dict in lst_data:
                    iden = dict["id"]
                    id_lst.append(iden)

                html_lst = """
                <ul>\n
                """
                for gene_id in id_lst:
                    dct = get_json_data(f"/lookup/id/{gene_id}", "")
                    if "display_name" in dct.keys():
                        gene_name = dct["display_name"]
                    else:
                        gene_name = gene_id + " (gene name not found)"
                    html_lst += f"<li>{gene_name}</li>\n"
                html_lst += "</ul>"
                list_genesdct = {"start": st, "end": end, "chr": chr, "gene_names": html_lst}
                body = read_html_file("medium_list.html").render(changes=list_genesdct)

        except Exception:
            self.send_response(404)
            body = Path("html/error.html").read_text()
        self.send_header("Content-Type", c_type)
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