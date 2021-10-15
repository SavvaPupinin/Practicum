import os, shutil, sys
with open("config.txt", "r") as file:
    default_folder = file.readline()

class Explorer(object):
    def __init__(self,default_folder):
        self.root = default_folder

    def path_reader(self, path):
        if path[0] == r"/" or path[0] == "\\":
            return self.root + path
        elif path[0:2] == ".." and os.getcwd() == self.root:
            return path[1:]
        else:
            return path

    def create_dir(self, dir_name):
        try:
            os.makedirs(self.path_reader(dir_name))
        except OSError as err:
            print(err)

    def remove_dir(self, dir_name):
        try:
            shutil.rmtree(self.path_reader(dir_name))
        except OSError as err:
            print(err)

    def change_dir(self, dir_name):
        try:
            os.chdir(self.path_reader(dir_name))
        except OSError as err:
            print(err)
        

    def touch(self, filename):
        try:
            with open(self.path_reader(filename), "w"):
                pass
        except OSError as err:
            print(err)
        

    def write_data(self, filename):
        with open(self.path_reader(filename), "w") as file:
            while True:
                try:
                    file.write(input()+'\n')
                except EOFError:
                    break

    def read_data(self, filename):
        try:
            with open(self.path_reader(filename), 'r') as file:
                    for line in file.readlines():
                        print(line, end = '')
        except OSError as err:
            print(err)

    def remove_f(self, filename):
        try:
            os.remove(self.path_reader(filename))
        except OSError as err:
            print(err)

    def copy_file(self,file1,file2):
        file1 = self.path_reader(file1)
        file2 = self.path_reader(file2)
        if sys.platform == 'win32':
            os.system(f'copy "{file1}" "{file2}"')
        else:
            os.system(f'cp -r {file1} {file2}')

    def replace_file(self,file1,file2):
        file1 = self.path_reader(file1)
        file2 = self.path_reader(file2)
        try:
            os.replace(file1, file2)
        except OSError as err:
            print(err)
        
    def rename_file(self,file1,file2):
        file1 = self.path_reader(file1)
        file2 = self.path_reader(file2)
        try:
            os.rename(file1, file2)
        except OSError as err:
            print(err)

            
command_string = """create_d -- создать директорию
delete_d -- удалить директорию
change -- сменить директорию
make_f -- создать файл
write_f -- записать в файл
read_f -- прочитать из файла
remove_f -- удалить файл
copy_f -- скопировать файл
replace_f -- переместить файл
rename_f -- переименовать файл
exit -- завершить работу"""
print(command_string)
explorer = Explorer(default_folder)
while True:
    command = input((os.getcwd() + "\\").replace(default_folder, "") + ":$ ").split()

    if command[0] == "create_d":
        explorer.create_dir(command[1])
    elif command[0] == "delete_d":
        explorer.remove_dir(command[1])
    elif command[0] == "change":
        explorer.change_dir(command[1])
    elif command[0] == "make_f":
        explorer.touch(command[1])
    elif command[0] == "write_f":
        explorer.write_data(command[1])
    elif command[0] == "read_f":
        explorer.read_data(command[1])
    elif command[0] == "remove_f":
        explorer.remove_f(command[1])
    elif command[0] == "copy_f":
        explorer.copy_file(command[1], command[2])
    elif command[0] == "replace_f":
        explorer.replace_file(command[1], command[2])
    elif command[0] == "rename_f":
        explorer.rename_file(command[1], command[2])

    elif command[0] == 'exit':
        break

    
    