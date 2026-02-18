from pathlib import Path

filename = "../Homo_sapiens_RNU6_269P_sequence.fa"
contents = Path(filename).read_text()

index = contents.find("\n")
print(contents[: index])