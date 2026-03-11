import socket
from Seq1 import Seq
ip = "127.0.0.1"
port = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((ip,port))
ls.listen()
print("The server is configured")

genes = ["AGAGAG", "ATCATATAGAG", "CCCCTTTTG", "CCCCCCGGGA"]

while True:
    print("Waiting for clients to connect")
    try:
        (client_s, c_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = client_s.recv(2048)
        real_msg = msg_raw.decode()
        r = real_msg.strip().split(" ",1)
        comd = r[0]
        print(comd)
        if comd == "PING":
            client_s.send("OK!\n".encode())
        elif comd == "GET":
            seq = genes[int(r[1])]
            client_s.send((seq + "\n").encode())
            print(seq)
        elif comd == "INFO":
            seq = Seq(r[1])
            s = f"Sequence: {str(seq)}\n"
            print(s)

            total = seq.len()
            l = s + f"Total length: {total}\n"
            print(l)

            dict_bases = seq.count()
            for base, count in dict_bases.items():
                pct = round((count / total) * 100, 1)
                ans = f"{base}: {count} ({pct}%)\n"
                print(ans)
                l += ans
            client_s.send(l.encode())
        elif comd == "COMP":
            seq = Seq(r[1])
            comp = seq.complement() + "\n"
            print(comp)
            client_s.send(comp.encode())
        elif comd == "REV":
            seq = Seq(r[1])
            rev = seq.reverse() + "\n"
            print(rev)
            client_s.send(rev.encode())
        elif comd == "GENE":
            gene_name = r[1]
            file_name = gene_name + ".txt"
            seq = Seq()
            seq.read_fasta(file_name)
            print(str(seq) + "\n")
            client_s.send((str(seq) + "\n").encode())