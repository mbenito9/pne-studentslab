from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

l = [s1, s2, s3]

for sequence in l:
    i = l.index(sequence)
    length = sequence.len()
    print(f"Sequence {i}: (Length: {length}) {sequence}")
    dct = sequence.count()
    print(" Bases:", dct)
    print(" Reverse:", sequence.reverse())