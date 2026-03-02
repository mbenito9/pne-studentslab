from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

sequence = Seq()
sequence.read_fasta("U5.txt")

length = sequence.len()
print(f"Sequence: (Length: {length}) {sequence}")
dct = sequence.count()
print(" Bases:", dct)
print(" Reverse:", sequence.reverse())
print(" Complement:", sequence.complement())