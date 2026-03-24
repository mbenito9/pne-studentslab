import random
import socket

class NumberGuesser:
    def __init__(self, secret_number, attempts):
        self.secret_number = secret_number
        self.attempts = attempts
    def __str__(self):
        return self.secret_number, self.attempts
    def guess(self, number):
        if number == self.secret_number:
            result = f"You won after {len(self.attempts)} attempts"
        else:
            if number < self.secret_number:
                result = "Higher"
            else:
                result = "Lower"
            self.attempts.append(number)
        return result, self.attempts

ip = "127.0.0.1"
port = 8082

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((ip,port))
ls.listen()
n = random.randint(0, 100)
attempts_lst = []

while True:
    print("Waiting for clients")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped")
        ls.close()
        exit()
    else:
        print(n)
        game = NumberGuesser(n, attempts_lst)
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        att_n = int(msg)
        attempt, lst_attempts = game.guess(att_n)
        if len(lst_attempts) <= 20:
            send = attempt + "\n" + f"Numbers tried: {lst_attempts} "
            cs.send(send.encode())
            if attempt != "Lower" and attempt != "Higher":
                cs.close()
        else:
            s = "You are too bad for this game, try again!"
            cs.send(s.encode())
            cs.close()