import http.client
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

dict_info = json.loads(data1)
people_lst = dict_info["people"]
print(f"Total people in the database: {len(people_lst)}")

for person in people_lst:
    name = person["Firstname"] + " " + person["Lastname"]
    print(f"Name: {name}\nAge: {person["age"]}")
    ph_num = person["phoneNumber"]
    print(f"Phone numbers: {len(ph_num)}")
    for i, num in enumerate(ph_num):
        print(f"\tPhone {i}:")
        print(f"\t\tType: {num["type"]}")
        print(f"\t\tNumber: {num["number"]}")
    print("")