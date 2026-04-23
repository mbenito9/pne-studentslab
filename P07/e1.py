import http.client
import json

server = "rest.ensembl.org"
endp = "/info/ping"
params = "?content-type=application/json"
url = server  + endp + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

conn = http.client.HTTPSConnection(server)
conn.request("GET", endp + params)
ans = conn.getresponse()
data = json.loads(ans.read().decode())
print(f"Response received: {ans.status} {ans.reason}\n")

if data["ping"]  == 1:
    print("ALIVE!")