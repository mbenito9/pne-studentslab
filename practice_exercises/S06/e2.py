class Seq:
    def __init__(self, strbases):
        self.bases = strbases
        b = ["A", "G", "C", "T"]
        non_valid = 0
        for i in self.bases:
            if i not in b:
                non_valid += 1
        if non_valid == 0:
            print("New sequence created")
        else:
            print("ERROR")
            self.bases = "Incorrect sequence entered"
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)

def print_seqs(list_seqs):
    for seq in list_seqs:
        index = list_seqs.index(seq)
        print(f"Sequence {index}: (Length: {seq.len()}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)