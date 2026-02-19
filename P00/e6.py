from Seq0 import *

u5 = "Amphiprion_ocellaris_U5_sequence.fa"
seq_u5 = seq_read_fasta(u5)

print("------| Exercise 6 |------")
print("Gene U5")
print(f"Fragment: {seq_u5[:20]}")
print(f"Reverse: {seq_reverse(seq_u5, 20)}")