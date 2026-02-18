from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    read = Path(filename).read_text()
    index = read.find("\n")
    string = read[index::]
    final = string.replace("\n", "")
    return final

if __name__== "__main__":
    seq_ping()