import socket, random, threading, csv

def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

def listening(sock):
    while True:
        msg = sock.recv(1024).decode()
        msg = decrypt(K, msg)
        print(msg)



def read_K():

    try:
        with open(f"{addr[0]}.txt", "r") as newfile:
            K = int(newfile.readline())
        conn.send("0;0;0".encode())
        B = int(conn.recv(1024).decode())

    except FileNotFoundError:
        a, g, p = [random.randint(1000,10000) for _ in range(3)]
        A = pow(g, a) % p
        conn.send(f"{g};{p};{A}".encode())
        B = int(conn.recv(1024).decode())
        K = pow(B, a) % p

        with open(f"{addr[0]}.txt", "w") as newfile:
            newfile.write(str(K))

    return K, B


def client_checker(B):
    with open("разрешено.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        for row in reader:
            if int(row[0]) == B:
                return True
        else:
            return False




port = 6666
sock = socket.socket()
sock.bind(('', port))
print(f"Слушается {port} порт")
sock.listen(0)
conn, addr = sock.accept()

K, B = read_K()


if client_checker(B):

    port = random.randint(1024,65535)
    conn.send(encrypt(K, str(port)).encode())
    sock.close()
    sock = socket.socket()
    sock.bind(('', port))
    print(f"Слушается {port} порт")
    sock.listen(0)
    conn, addr = sock.accept()

    threading.Thread(target = listening, args = (conn, ), daemon = True).start() 

    while True:
        cmd = input()
        if cmd == "stop":
            break
        cmd = encrypt(K, cmd)
        conn.send(cmd.encode())
else:
    print("Не разрешен такой клиент")

sock.close()