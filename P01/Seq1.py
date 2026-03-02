from pathlib import Path

class Seq:
    def __init__(self, strbases=None):
        self.bases = strbases
        if strbases is not None:
            b = ["A", "G", "C", "T"]
            non_valid = 0
            for i in self.bases:
                if i not in b:
                    non_valid += 1
            if non_valid == 0:
                print("New sequence created")
            else:
                print("INVALID sequence")
                self.bases = "ERROR"
        else:
            print("NULL sequence created")
            self.bases = "NULL"
    def __str__(self):
        return self.bases
    def len(self):
        if self.bases == "ERROR":
            result = 0
        elif self.bases == "NULL":
            result = 0
        else:
            result = len(self.bases)
        return result
    def count_base(self,base):
        if self.bases != "ERROR" and self.bases != "NULL":
            count = 0
            for i in self.bases:
                if i == base:
                    count += 1
            c = count
        else:
            c = 0
        return c
    def count(self):
        dct = {"A": 0, "T": 0, "C": 0, "G": 0}
        if self.bases != "NULL" and self.bases != "ERROR":
            for i in self.bases:
                dct[i] += 1
        return dct
    def reverse(self):
        if self.bases == "NULL":
            f = "NULL"
        elif self.bases == "ERROR":
            f = "ERROR"
        else:
            f = self.bases[::-1]
        return f
    def complement(self):
        if self.bases == "NULL":
            new_seq = "NULL"
        elif self.bases == "ERROR":
            new_seq = "ERROR"
        else:
            bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            new_seq = ""
            for i in self.bases:
                complement = bases[i]
                new_seq += complement
        return new_seq
    def read_fasta(self,filename):
        if self.bases == "NULL":
            folder = "sequences/"
            complete = folder + filename
            read = Path(complete).read_text()
            index = read.find("\n")
            string = read[index::]
            final = string.replace("\n", "")
            self.bases = final


