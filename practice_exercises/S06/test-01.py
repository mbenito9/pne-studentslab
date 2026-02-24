class Seq:
    def __init__(self, strbases):
        self.bases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)
s1 = Seq("ACGACT")
s2 = Seq("TTTTT")
print(f"String: {s1}, Length: {s1.len()}")
print(f"String: {s2}, Length: {s2.len()}")

class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")
    def __str__(self):
        return self.name

g = Gene("ACTTT", "created_gene")
print(g)