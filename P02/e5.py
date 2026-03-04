from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 5 |------")
port = 8080
ip = "212.128.255.76"

c = Client(ip, port)
gene = "FRAT1"
s = Seq()
s.read_fasta(gene + ".txt")
send_frat = c.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
print(f"Gene FRAT1: {s}")
frag = ""
count = 0
for i in str(s):
    if len(frag) < 10:
        frag += i
    else:
        count += 1
        message = f"Fragment {count}: {frag}"
        print(message)
        m_frag = c.talk(message)
        frag = ""
        frag += i
    if count == 5:
        break

