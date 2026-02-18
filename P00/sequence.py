from pathlib import Path

ada = "../Homo_sapiens_ADA_ch20.fa"
ada_cont = Path(ada).read_text()

index = ada_cont.find("\n")
string = ada_cont[index::]
final = string.replace("\n", "")

print("Total bases:", len(final))