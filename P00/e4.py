from Seq0 import *

bases = ["A", "C", "G", "T"]

u5 = "Amphiprion_ocellaris_U5_sequence.fa"
frat1 = "Homo_sapiens_FRAT1_sequence.fa"
fxn = "FXN_chD4.fa"
ada = "Homo_sapiens_ADA_ch20.fa"

dct = {"U5": u5, "ADA": ada, "FRAT1": frat1, "FXN": fxn}

for gene, filename in dct.items():
    cleared = seq_read_fasta(filename)
    print("Gene:", gene)
    for i in bases:
        print(f"{i}: {seq_count_base(cleared, i)}")