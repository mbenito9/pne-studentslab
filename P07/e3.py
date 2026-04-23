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
termcolor.cprint("Gene:", "green", end=" ")
print("MIR633")

termcolor.cprint("Description: ", "green", end=" ")
print(dict_data["desc"])
termcolor.cprint("Bases:", "green", end=" ")
print(dict_data["seq"])