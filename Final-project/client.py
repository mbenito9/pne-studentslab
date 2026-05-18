import http.client
import json
import termcolor

server = "localhost"
port = 8081
endp = [
"/listSpecies?limit=10",
"/listSpecies?limit=",
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
        link += "&json=1"
        print(link)
        conn.request("GET", link)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        dct_json = json.loads(data)
        for key, value in dct_json.items():
            key = key.replace("_", " ")
            key = str.upper(key)
            print(key)
            print(f"\t{value}")
except ConnectionRefusedError:
    print("error, cannot connect to the server")