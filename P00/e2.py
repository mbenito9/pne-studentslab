from Seq0 import seq_read_fasta

u5 = "Amphiprion_ocellaris_U5_sequence.fa"
sequence = seq_read_fasta(u5)

print("DNA file:", u5)
print("First 20 bases:", sequence[:20])