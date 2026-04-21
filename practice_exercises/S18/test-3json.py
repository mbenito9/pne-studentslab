import json
from pathlib import Path

json_str = Path("people-3.json").read_text()
info = json.loads(json_str)

phone_lst = info["phoneNumber"]

for c in phone_lst:
    print(f"Number: {c["number"]} Type: {c["type"]}")