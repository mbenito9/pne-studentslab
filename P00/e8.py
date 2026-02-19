from Seq0 import *

def limit_val(lst):
    min_v = lst[1]
    max_v = 0
    for i in lst:
        if i > max_v:
            max_v = i
        elif i < min_v:
            min_v = i
    return max_v, min_v

if __name__ == "__main__":
    u5 = "Amphiprion_ocellaris_U5_sequence.fa"
    frat1 = "Homo_sapiens_FRAT1_sequence.fa"
    fxn = "FXN_chD4.fa"
    ada = "Homo_sapiens_ADA_ch20.fa"

    dct = {"U5": u5, "ADA": ada, "FRAT1": frat1, "FXN": fxn}

    print("-----| Exercise 8 |------")

    for gene, filename in dct.items():
        cleared = seq_read_fasta(filename)
        dict_bases = seq_count(cleared)
        lst = []
        for base, number in dict_bases.items():
            lst.append(number)
        most_freq, less_freq = limit_val(lst)
        for base in dict_bases.keys():
            if dict_bases[base] == most_freq:
                print(f"Gene {gene}: Most frequent base: {base}")