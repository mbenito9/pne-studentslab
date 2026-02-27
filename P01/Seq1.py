from pathlib import Path

class Seq:
    def __init__(self, strbases=None):
        self.bases = strbases
        if strbases != None:
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