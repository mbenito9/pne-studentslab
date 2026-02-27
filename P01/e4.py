from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

l = [s1, s2, s3]

print("-----| Practice 1, Exercise 4 |------")
for i in l:
    index = l.index(i)
    length = i.len()
    print(f"Sequence {index + 1}: (Length: {length}) {i}")