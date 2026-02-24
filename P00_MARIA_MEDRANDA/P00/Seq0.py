from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    folder = "sequences/"
    complete = folder + filename
    read = Path(complete).read_text()
    index = read.find("\n")
    string = read[index::]
    final = string.replace("\n", "")
    return final

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count

def seq_count(seq):
    dct = {"A": 0 , "T": 0, "C": 0, "G": 0}
    for i in seq:
        dct[i] += 1
    return dct

def seq_reverse(seq, n):
    cut = seq[:n]
    return cut[::-1]

def seq_complement(seq):
    bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
    new_seq = ""
    for i in seq:
        complement = bases[i]
        new_seq += complement
    return new_seq
