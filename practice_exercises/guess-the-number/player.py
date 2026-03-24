from Client0 import Client

ip = "127.0.0.1"
port = 8082

flag = True

while flag:

    number = str(input("Try a number!"))
    client = Client(ip,port)
    ans = client.talk(number)
    print(ans)
    if "Higher" not in ans and "Lower" not in ans:
        flag = False