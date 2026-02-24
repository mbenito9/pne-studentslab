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

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")