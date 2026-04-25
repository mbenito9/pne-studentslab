import http.client
import json
import termcolor

genes = {"MIR633": "ENSG00000207552"}

server = "rest.ensembl.org"
endp = f"/sequence/id/{genes["MIR633"]}"
params = "?content-type=application/json"
url = server  + endp + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

conn = http.client.HTTPSConnection(server)
conn.request("GET", endp + params)
ans = conn.getresponse()
dict_data = json.loads(ans.read().decode())

print(f"Response received: {ans.status} {ans.reason}\n")
print(f"{termcolor.colored("Gene:", "green")} MIR633")

print(f"{termcolor.colored("Description:", "green")} {dict_data["desc"]}")

print(f"{termcolor.colored("Bases:", "green")} {dict_data["seq"]}")