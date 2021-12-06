import socket
import os
import shutil
import csv
import re

'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cd <path> - перемещение по директориям
mkdir <dirname> - создать директорию (рекурсивно)
rmtree <dirname> - удалить директорию (рекурсивно)
touch <filename> - создать пустой файл
remove <filename> - удалить файл
cat <filename> - отправляет содержимое файла
get_file <filename> - отправляет файл в текущую директорию у клиента
send_file <filename> - принимает файл с текущей директории клиента
'''


def path_decoder(root, current, dir_):
    if current == "\\" and dir_[:2] == "..":

        return root + dir_[2:]
    elif dir_[0] in ["\\", "/"]:
        dir_ = re.sub(r"^[\\/]+", "", dir_)
        logging(dir_)
        return os.path.join(root, dir_)
    else:
        return os.path.join(root, current[1:], dir_)

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def logging(*strings):
    print(*strings)
    with open(logName, "a") as logfile:
        logfile.write(" ".join([str(item) for item in strings]) + "\n")


def authorization(message):
    global usersDatabase, root
    login, message = message.split("&lgn&", 1)
    password, message = message.split("&pswd&", 1)
    users_dir, message = message.split("&crdir&", 1)
    size, message = message.split("&fsize&", 1)
    if login == password == "admin":
         user_root = root
    else:
        user_root =  os.path.join(root, login)
        with open(usersDatabase, "a+", newline = "") as csvfile:
            csvfile.seek(0,0)
            reader = csv.reader(csvfile, delimiter = ";")
            for line in reader:
                if line[0] == login:
                    if line[1] == password:
                        break
                    else:
                        return None
            else:
                writer = csv.writer(csvfile, delimiter = ";")
                writer.writerow([login, password])

        try: 
            os.makedirs(user_root)
        except FileExistsError:
            pass

    return user_root, users_dir, message, size


def try_decorator(path_func):
    def wrapper(*path):
        try:
            retvalue = path_func(*path)
            if retvalue == None:
                return "Успешно выполнено"
            else:
                return retvalue
        except FileNotFoundError:
            return (f'Неверный путь')
        except FileExistsError:
            return (f'Уже существует') 
        except PermissionError:
            return f"Ошибка доступа"
    return wrapper

def pwd(dirname):
    return os.path.join(dirname)

def ls(path):
    return '\n\r'.join(os.listdir(path))

def cd(path, current, root):
    try:
        os.chdir(path)
    except:
        return current
    return os.getcwd().replace(root,"")+"\\"
    

@try_decorator
def mkdir(path):
    os.makedirs(path)

@try_decorator
def rmtree(path):
    shutil.rmtree(path)

@try_decorator
def remove(path):
    os.remove(path)

@try_decorator
def touch(path):
    with open(path, 'x'):
        pass

@try_decorator
def cat(path):
    with open(path, "r") as file:
        return "\n\r".join(file.readlines())

@try_decorator
def rename(path1, path2):
    os.rename(path1, path2)

def get_file(path):
    global conn, END, ERROR
    try:
        with open(path, "rb") as bytefile:
            while read_bytes := bytefile.read(1024):
                conn.send(read_bytes)

    except FileNotFoundError:
        retvalue = 'Неверный путь'.decode()+ERROR
    except PermissionError:
        retvalue = "Ошибка доступа".decode()+ERROR
    else:
        retvalue = END
    logging("Has been sent")
    return retvalue

def send_file(path, root, size):
    global conn, END, ERROR
    available = pow(2,20)*10 - get_size(root) 
    print(available, int(size))
    if available < int(size):
        return "Мало места на диске!"
    else:
        conn.send(b"$ENOUGHT$")
    searcher = conn.recv(1024)
    with open (path, "wb") as bytefile:
            while True:
                if END in searcher:
                    bytefile.write(searcher.replace(END, b""))
                    break
                else:
                    bytefile.write(searcher)
                    searcher = conn.recv(1024)
    logging("Получено")
    return "успешно загружено"




def process(req):
    req = authorization(req)
    if req:
        user_root, users_dir, req, size = req
        req, *dir_ = req.split()
        path = [path_decoder(user_root, users_dir, item) for item in dir_]
        if not path:
            path = [""]

        if req == 'pwd':
            return pwd(users_dir)
        elif req == 'ls':
            return ls(os.path.join(user_root, users_dir[1:]))
        elif req == "cd":
            return cd(path[0], users_dir, user_root)
        elif req == 'mkdir':
           
            return mkdir(path[0])
        elif req == 'rmtree':
            return rmtree(path[0])
        elif req == 'touch':
            return touch(path[0])
        elif req == 'remove':
            return remove(path[0])
        elif req == 'cat':
            return cat(path[0])
        elif req == 'rename':
            return rename(*path[:2])
        elif req == "get_file":
            return get_file(path[0])
        elif req == "send_file":
            return send_file(path[0], user_root, size)

        else:
            return 'Не такой команды'
    else:
        return "Неверный пароль"






END = b"&END"
ERROR = b'&ERROR'
PORT = 8090
root = os.path.join(os.getcwd())
usersDatabase = os.path.join(root, "users.csv")
logName = os.path.join(root, "log.txt")
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
logging("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    logging("request:", request)
    
    response = process(request)
    logging("response:", response)
    if not response:
        response = "\00"
    try:
        conn.send(response.encode())
    except AttributeError:
        conn.send(response)

