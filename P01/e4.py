from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

l = []
l.append(s1)
l.append(s2)
l.append(s3)

for i in l:
    length = len(i)
    print(f"Sequence {index + 1}: {i}")