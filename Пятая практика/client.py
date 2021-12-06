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


def myKeys():
    with open("myKey.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        return [int(i) for i in next(reader)]



def create_K():

    from_server = sock.recv(1024).decode().split(";")
    from_server = [int(i) for i in from_server]
    try:
        K, B = myKeys()
    except FileNotFoundError:
        b = random.randint(100,999)
        g = from_server[0]
        p = from_server[1]
        B = pow(g, b) % p
        A = from_server[2]
        K = pow(A, b) % p

        with open("myKey.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile, delimiter = ";")
            writer.writerow([K, B])
    sock.send(str(B).encode())
    return K


sock = socket.socket()
port = 6666
sock.connect(('localhost', port))
print(f"Слушаю порт {port}")

K = create_K()

port = int(decrypt(K,sock.recv(1024).decode()))
sock.close()
sock = socket.socket()
sock.connect(('localhost', port))
print(f"Слушаю порт {port}")

threading.Thread(target = listening, args = (sock, ), daemon = True).start()

while True:
    cmd = input()
    if cmd == "stop":
        break
    cmd = encrypt(K, cmd)
    sock.send(cmd.encode())

sock.close()