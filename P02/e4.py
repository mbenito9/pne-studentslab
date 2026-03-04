from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 4 |------")
port = 8080
ip = "212.128.255.76"

c = Client(ip, port)
genes = ["U5", "ADA", "FRAT1"]
for i in genes:
    s = Seq()
    s.read_fasta(i + ".txt")
    m = f"Sending the {i} gene to the server..."
    print(f"To the server: {m}")
    first_m = c.talk(m)
    print(f"From the server: {first_m}")
    print(f"To the server: {s}")
    ans = c.talk(str(s))
    print(f"From the server: {ans}")
