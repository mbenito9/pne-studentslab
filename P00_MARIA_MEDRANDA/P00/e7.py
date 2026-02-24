from Seq0 import *

u5 = "Amphiprion_ocellaris_U5_sequence.fa"
seq_u5 = seq_read_fasta(u5)
cut_seq = seq_u5[:20]

print("-----| Exercise 7 |------")
print("Gene U5")
print(f"Frag: {cut_seq}")
print(f"Comp: {seq_complement(cut_seq)}")

