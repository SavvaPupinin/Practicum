import socket
import re
import os

HOST = 'localhost'
PORT = 8090
END = b"&END"
ERROR = b'&ERROR'
login = input("Введите логин: ")
password = input("Введите пароль: ")
# login = "admin"
# password = "admin"
current_directory = "\\"

def creator(message, size=0):
    global login, password, current_directory
    return f"{login}&lgn&{password}&pswd&{current_directory}&crdir&{size}&fsize&{message}".encode()


def reciver(request):
    global sock, ERROR, END
    
    qualifier = sock.recv(1024)
    if ERROR in qualifier:
        print((qualifier.replace(ERROR, b"")).decode())
    else:
        filename = re.split("[ \\/]+", request)[-1]
        with open (filename, "wb") as bytefile:
            while True:
                if END in qualifier:
                    qualifier= qualifier.split(END)[0]
                    bytefile.write(qualifier)
                    break
                else:
                    bytefile.write(qualifier)
                    qualifier = sock.recv(1024)
    

def sender(request):
    global sock, END
    filename = re.split("[ \\/]+", request)[-1]
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        sock.send(creator(request, size))
        space_allower = sock.recv(1024).decode()
        if space_allower != '$ENOUGHT$':
            print(space_allower)
            return
        with open(filename, "rb") as bytefile:
    
            while read_bytes := bytefile.read(1024):
                sock.send(read_bytes)
        sock.send(END)
    else:
        print("Нет такого файла")
    print(sock.recv(1024).decode())

while True:
    request = input(current_directory+'>')
    request = request.strip()
    if request == "exit":
        print("goodbye")
        break
    sock = socket.socket()
    sock.connect((HOST, PORT))
    if request[:9] == "send_file":
        if request == "send_file":
            print("Нет такого файла")
        else:
            sender(request)
    else:
        sock.send(creator(request))
        if request[:9] == "get_file " or request == "get_file":
            reciver(request)
        else:
            response = sock.recv(1024).decode()
            # print("recieved:", response)
            if request[:3] == "cd " or request == "cd":
                current_directory = response
            else:
                print(response)
    
    sock.close()