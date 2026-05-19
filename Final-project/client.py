import http.client
import json
import termcolor

server = "localhost"
port = 8080
endp = [
"/listSpecies?limit=10",
"/listSpecies",
"/karyotype?species=mouse",
"/karyotype?species=Shrew+mouse",
"/chromosomeLength?species=mouse&chromo=18",
"/geneLookup?gene=FRAT1",
"/geneSeq?gene=FRAT1",
"/geneInfo?gene=FRAT1",
"/geneCalc?gene=FRAT1",
"/geneList?chromo=9&start=22125500&end=22136000",
]

conn = http.client.HTTPConnection(server, port)
try:
    for link in endp:
        if "=" in link:
            link += "&"
        else:
            link += "?"
        link += "json=1"
        print(f"\nRequested end point: {link}")
        conn.request("GET", link)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        dct_json = json.loads(data)
        for key, value in dct_json.items():
            if key == "chr" or key == "chroms":
                key = "chromosome(s)"
            elif key == "len":
                key = "total length"
            elif key == "start" or key == "end":
                key += " point"
            key = key.replace("_", " ")
            key = str.upper(key)
            termcolor.cprint(key + ":", "green")
            if type(value) == list:
                for i in value:
                    termcolor.cprint(f"\t{i}", "blue")
            else:
                termcolor.cprint(f"\t{value}", "blue")
except ConnectionRefusedError:
    print("error, cannot connect to the server")