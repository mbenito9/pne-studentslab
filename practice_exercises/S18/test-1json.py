import json
import termcolor
from pathlib import Path

#json in str #json from file: json.load()
json_str = Path("people-1.json").read_text()

#create an object with the people info from the object, and the info is stored as a dictionary

person = json.loads(json_str)

fname = person["Firstname"]
lname = person["Lastname"]
age = person["Age"]
print(f"Name: {fname} {lname}")
