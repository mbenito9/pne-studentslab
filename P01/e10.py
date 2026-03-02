from Seq1 import Seq

def limit_val(lst):
    min_v = lst[1]
    max_v = 0
    for i in lst:
        if i > max_v:
            max_v = i
        elif i < min_v:
            min_v = i
    return max_v, min_v

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    filename = gene + ".txt"
    seq = Seq()
    seq.read_fasta(filename)
    dct = seq.count()
    freq = []
    for value in dct.values():
        freq.append(value)
    most_n, least_n = limit_val(freq)
    most_bases = []
    for key in dct.keys():
        if dct[key] == most_n:
            most_bases.append(key)
    print(f"Gene {gene}: Most Frequent Base: {" and ".join(most_bases)}")