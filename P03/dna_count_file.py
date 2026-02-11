from dna_count import count_bases

f = open("dna.txt", "r")
linesn = f.readlines()
f.close() #remember to always close the file


if __name__ == "__main__":
    with open("dna.txt", "r") as f:
        lines = f.readlines() #when we get out of the with loop, the proper loop calls the close function

    total = 0
    bases = {"A": 0, "G": 0, "C": 0, "T": 0}
    for seq in lines:
        seq = seq.strip()
        #Remove blank spaces and end of line characters at the end of the string
        total += len(seq)
        result = count_bases(seq)
        for key in result:
            bases[key] += result[key]

    print("The total number is:", total)
    for base, c in bases.items():
        print(f"{base}: {c}")