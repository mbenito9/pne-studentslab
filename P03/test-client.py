from Client0 import Client

ip = "127.0.0.1"
port = 8080

client = Client(ip,port)
commands = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for i in commands:
    print(f" * TESTING {i}...")
    if i == "PING":
        ans = client.talk(i)
        print(ans)
    elif i == "GET":
        for j in range(5):
            get = i + f" {j}"
            seq = client.talk(get)
            print(f"{i} {j}: {seq}")
            if j == 0:
                get0 = seq
    elif i == "INFO" or i == "COMP" or i == "REV":
        ans = client.talk(i + " " + get0)
        if i != "INFO":
            print(i + " " + ans)
        else:
            print(ans)
    elif i == "GENE":
        for name in genes:
            gene_com = i + " " + name
            server_gen = client.talk(gene_com)
            print(gene_com)
            print(server_gen.strip())