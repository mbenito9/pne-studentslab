import termcolor

termcolor.cprint("Hey! this is printed in green!", 'green')

class Seq:
    def __init__(self, strbases):
        self.bases = strbases
        print("New sequence created")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)

def print_seqs(list_seqs, color):
    for seq in list_seqs:
        index = list_seqs.index(seq)
        final = f"Sequence {index}: (Length: {seq.len()}) {seq}"
        termcolor.cprint(final, color)

def generate_seqs(pattern, number):
    new_list = []
    new_list.append(pattern)
    c = 1
    new_seq = pattern
    while c < number:
        new_seq += pattern
        c += 1
        new_list.append(new_seq)
    return new_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

changed1 = []
for j in seq_list1:
    seq = Seq(j)
    changed1.append(seq)

changed2 = []
for i in seq_list2:
    seq = Seq(i)
    changed2.append(seq)


print("List 1:")
print_seqs(changed1, "blue")

print()
print("List 2:")
print_seqs(changed2, "green")