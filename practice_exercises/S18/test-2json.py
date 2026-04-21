import json
import termcolor
from pathlib import Path

json_str = Path("people-2.json").read_text()
info = json.loads(json_str)

lst_pn = info["phoneNumber"]

for i in lst_pn:
    print(f"Phone number {lst_pn.index(i) + 1}: {i}")