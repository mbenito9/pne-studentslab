from Seq0 import *

u5 = "Amphiprion_ocellaris_U5_sequence.fa"
frat1 = "Homo_sapiens_FRAT1_sequence.fa"
fxn = "FXN_chD4.fa"
ada = "Homo_sapiens_ADA_ch20.fa"

dct = {"U5": u5, "ADA": ada, "FRAT1": frat1, "FXN": fxn}

print("-----| Exercise 3 |------")
for gene, filename in dct.items():
    cleared = seq_read_fasta(filename)
    length = seq_len(cleared)
    print(f"Gene {gene} --> {length}")
