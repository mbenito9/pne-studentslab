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

def get_body(file, d):
    if "html" in file:
        c = read_html_file(file).render(changes=d)
        ty = "text/html"
    elif file == "json":
        c = json.dumps(d)
        ty = "application/json"
    return ty, c

port = 8081
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        analyse_path = urlparse(self.path)
        path = analyse_path.path
        arg = parse_qs(analyse_path.query)
        body = ""
        c_type = ""

        try:
            self.send_response(200)
            if "json" in arg.keys():
                json_arg = arg["json"][0]
            if "json" not in arg.keys():
                json_arg = 0
            if path == "/":
                body = Path("html/main_page.html").read_text()
                c_type = "text/html"
            elif path == "/listSpecies":
                dict_data = get_json_data("/info/species", "")
                lst_species = dict_data["species"]
                total = 0

                if "limit" in arg.keys():
                    limit = int(arg["limit"][0])
                else:
                    limit = 0

                name_lst = []
                for specie in lst_species:
                    name = specie["display_name"]
                    name_lst.append(name)
                    total += 1
                    if total == limit:
                        break

                dct = {"limit": limit, "total_species": len(lst_species)}

                if json_arg == "1":
                    dct["names"] = name_lst
                    c_type, body = get_body("json", dct)
                else:
                    req_species = """
                    <ul>\n
                    """
                    for name in name_lst:
                        req_species += f"<li>{name}</li>\n"
                    req_species += "</ul>"
                    dct["names"] = req_species
                    c_type, body = get_body("basic1.html", dct)

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

                    if json_arg == "1":
                        dct["chroms"] = karyo_lst
                        c_type, body = get_body("json", dct)

                    else:
                        c_type, body = get_body("basic2.html", dct)

                elif path == "/chromosomeLength":
                    n_chr = arg["chromo"][0]
                    lst_region = dict_data["top_level_region"]
                    for chromosome in lst_region:
                        if chromosome["name"] == n_chr:
                            length = chromosome["length"]
                    dct = {"number": n_chr, "len": length}

                    if json_arg == "1":
                        body = json.dumps(dct)
                        c_type = "application/json"
                    else:
                        body = read_html_file("basic3.html").render(changes=dct)
                        c_type = "text/html"

            elif path == "/geneLookup" or path == "/geneSeq" or path == "/geneInfo" or path == "/geneCalc":
                gene_name = arg["gene"][0]
                dict_data = get_json_data(f"/lookup/symbol/homo_sapiens/{gene_name}", "")
                iden = dict_data["id"]
                dct = {"id": iden, "gene": gene_name}
                file = ""
                if path == "/geneLookup":
                    file = "medium_id.html"

                if path == "/geneSeq" or path == "/geneCalc":
                    dict_data = get_json_data(f"/sequence/id/{iden}", "")
                    seq = dict_data["seq"]

                    if path == "/geneCalc":
                        object_seq = Seq(seq)

                        info_str = str(object_seq.info())
                        i = info_str.index("Most")
                        strp_info = info_str[:i]

                        dct["info"] = strp_info
                        file = "medium_calc.html"

                    if path == "/geneSeq":
                        dct["sequence"] = seq
                        file = "medium_seq.html"

                if path == "/geneInfo":
                    start = dict_data["start"]
                    end = dict_data["end"]
                    length = int(end) - int(start)
                    add = {"start": start, "end": end, "len": length, "chr": dict_data["seq_region_name"]}
                    dct.update(add)
                    file = "medium_Info.html"

                if json_arg == "1":
                    c_type, body = get_body("json", dct)
                if json_arg != "1":
                    c_type, body = get_body(file, dct)

            elif path == "/geneList":
                chr = arg["chromo"][0]
                st = arg["start"][0]
                end = arg["end"][0]
                lst_data = get_json_data(f"/overlap/region/human/{chr}:{st}-{end}", ";feature=gene")

                id_lst = []
                for dict in lst_data:
                    iden = dict["id"]
                    id_lst.append(iden)

                html_lst = []
                for gene_id in id_lst:
                    dct_data = get_json_data(f"/lookup/id/{gene_id}", "")
                    if "display_name" in dct_data.keys():
                        gene_name = dct_data["display_name"]
                    else:
                        gene_name = gene_id + " (gene name not found)"
                    html_lst.append(gene_name)
                dct = {"start": st, "end": end, "chr": chr, "gene_names": html_lst}
                file = "medium_list.html"
                if json_arg == "1":
                    c_type, body = get_body("json", dct)
                if json_arg != "1":
                    c_type, body = get_body(file, dct)
        except KeyboardInterrupt:
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