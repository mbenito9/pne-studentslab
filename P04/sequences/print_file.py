from pathlib import Path

filename = "../Amphiprion_ocellaris_U5_sequence.fa"

contents = Path(filename).read_text()

print(contents)