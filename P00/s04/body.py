from pathlib import Path

u5 = "../Amphiprion_ocellaris_U5_sequence.fa"
contents = Path(u5).read_text()

index = contents.find("\n")
print(contents[index::])