import http.client
import json
from Seq1 import Seq
import termcolor

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
         }
try:
    for gene, iden in genes.items():
        server = "rest.ensembl.org"
        endp = f"/sequence/id/{iden}"
        params = "?content-type=application/json"
        url = server  + endp + params

        print("")
        print(f"Server: {server}")
        print("URL: ", url)

        con = http.client.HTTPSConnection(server)
        con.request("GET", endp + params)
        ans = con.getresponse()
        print(f"Response received!: {ans.status} {ans.reason}\n")
        dict_data = json.loads(ans.read().decode())

        print(f"{termcolor.colored("Gene", "green")}: {gene}")
        print(f"{termcolor.colored("Description", "green")}: {dict_data["desc"]}")

        seq = Seq(dict_data["seq"])
        print(seq.info())
except ValueError:
    print("The gene entered is not in the database")