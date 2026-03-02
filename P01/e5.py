from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

l = [s1, s2, s3]

bases = ["A", "T", "C", "G"]

for sequence in l:
    i = l.index(sequence)
    length = sequence.len()
    print(f"Sequence {i}: (Length: {length}) {sequence}")
    c = 0
    for base in bases:
        c += 1
        if c != len(bases):
            print(f"    {base}: {sequence.count_base(base)}", end=",")
        else:
            print(f"    {base}: {sequence.count_base(base)}", end="\n")
