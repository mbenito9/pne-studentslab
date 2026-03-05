from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 6 |------")

ip = "212.128.255.76"
c1 = Client(ip, 8080)
c2 = Client(ip, 8081)
gene = "FRAT1"
s = Seq()
s.read_fasta(gene + ".txt")

send_frat1 = c1.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
send_frat2 = c2.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
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
        if count % 2 == 0:
            m_server2 = c2.talk(message)
        else:
            m_server1 = c1.talk(message)
        frag = ""
        frag += i
    if count == 10:
        break