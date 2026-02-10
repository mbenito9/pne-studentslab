from dna_count import count_bases

f = open("dna.txt", "r")
linesn = f.readlines()
f.close() #remember to always close the file

with open("dna.txt", "r") as f:
    lines = f.readlines() #when we get out of the with loop, the proper loop calls the close function

#for seq in linesn:
    #seq = seq.strip() #Remove blank spaces and end of line characters at the end of the string
total = 0
lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
new_str = ""
for i in lines:
    new_str += i

d = count_bases(new_str)
sum = 0
for key, value in d.items():
    sum += value
    print(f"{key}: {value}")
print(sum)
print(lines)
print(linesn)