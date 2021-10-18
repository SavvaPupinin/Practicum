import socket, getpass, sys, random, csv, threading, os, time

LOCK = threading.Lock()
L_FLAG = True

def send1(sock, data):
    sock.send(data.encode())

def recv1(sock, vol):
    data = sock.recv(vol).decode()
    return data

socket.socket.send1 = send1
socket.socket.recv1 = recv1

def logging(*data):
    data = ' '.join((str(item) for item in data))
    global LOCK, L_FLAG
    if L_FLAG:
        with LOCK:
            print(data)
            with open("log.txt", 'a+') as file:
                file.write(data+'\n')

logging("Запуск сервера")
sock = socket.socket()
port = 9090

while True:
    try:
        sock.bind(('', port))
        logging(f"Порт {port}")
        break
    except OSError as oserr:
        logging(f"порт {port} недоступен")
        port = random.randint(1024,65535)

sock.listen(0)
logging("Начало прослушивания порта")


def lstn(conn, addr):
        global users_list, LOCK, history
        logins = "logins.csv"
        try:
                with LOCK:
                        with open(logins, 'a+', newline = '') as login:
                                login.seek(0,0)
                                reader = csv.reader(login, delimiter = ';')
                                for row in reader:
                                        if row[0] == addr[0]:
                                                password = row[2]
                                                name = row[1]
                                                break
                                else:
                                        conn.send1("Введите имя")
                                        name = conn.recv1(1024)
                                        conn.send1("Придумайте пароль")
                                        password = conn.recv1(1024)
                                        writer = csv.writer(login, delimiter = ';')
                                        writer.writerow([addr[0], name, password])

                while True:
                        conn.send1("Введите пароль для старта")
                        password1 = conn.recv1(1024)
                        if password1 == password:
                                conn.send1((f"Начинаем общение {name}"))

                                break
                        else:
                                conn.send1("Неверный пароль")
                

                while True:
                        data = conn.recv1(1024)
                        logging(name, " ~ ", data)
                        with LOCK:
                                with open(history, "a+") as file:
                                        file.write(name+": "+data+"\n")
                        for conn1 in users_list:
                                if conn1 != conn:
                                        conn1.send1(name+": "+data)
                        
        except:
                users_list.remove(conn)
                raise                


def connecting():
        global users_list, CON_FLAG
        while True:
                if CON_FLAG:
                        conn, addr = sock.accept()
                        logging(f"Подключение клиента {addr}")
                        users_list.append(conn)
                        threading.Thread(target = lstn, args = (conn, addr), daemon = True).start()

users_list = []

CON_FLAG = True
history = f"history_{time.time()}.txt"
threading.Thread(target = connecting, daemon = True).start()

while True:
        inpt = input()
        if inpt == "выкл":
                break
        elif  inpt == "показывать":
                L_FLAG = True
        elif  inpt == "не показывать":
                L_FLAG = False
        elif inpt == "очистить":
                if os.name == 'nt':
                        os.system('cls')
                else:
                        os.system('clear')
                with LOCK:
                        with open("log.txt", "w"):
                                pass
        elif inpt == "удалить клиентов":
                with LOCK:
                        with open("logins.csv", "w"):
                                pass
        elif inpt == "заморозить":
                CON_FLAG = False
        elif inpt == "разморозить":
                CON_FLAG = True
logging("Остановка сервера")

