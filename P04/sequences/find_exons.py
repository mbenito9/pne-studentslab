from pathlib import Path

ada_exons = "../ada_exons.fa"
ada_exons = Path(ada_exons).read_text()
ada = "../Homo_sapiens_ADA_ch20.fa"
ada_cont = Path(ada).read_text()

while flag:
    index = ada_exons.find("\n")
    ada_exons = ada_exons[index::]