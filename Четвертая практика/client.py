import socket, getpass, threading
from time import sleep

def send1(sock, data):
    sock.send(data.encode())

def recv1(sock, vol):
    data = sock.recv(vol).decode()
    return data

socket.socket.send1 = send1
socket.socket.recv1 = recv1

def recieving():
    while True:
        data = sock.recv1(1024)
        with LOCK:
            print(data)


LOCK = threading.Lock()
sock = socket.socket()
sock.setblocking(1)



host, port = 'localhost', 9090
print("Соединение с сервером")
sock.connect((host, port))
print("Соединено с сервером")


threading.Thread(target = recieving, daemon = True).start()
while True:
    msg = input()
    sock.send1(msg)
    if msg == "exit":
        break
        

print("Разрыв соединения с сервером")



sock.close() 