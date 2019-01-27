try:
    import lesson05.p_solution.hw05_normal as normal
except ModuleNotFoundError:
    import hw05_normal as normal

import os
import sys
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

print('sys.argv = ', sys.argv)


def print_help():
    print('''We have this commands:
                 "cd %PATH%" - Change directory by path like "C:\\Windows"
                 "ls" - See current directory content
                 "rm %DIR_NAME%" - Remove directory
                 "mkdir %DIR_NAME%" - Make directory
                 "help" - show this help
                 "ping" - test ''')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy():
    path = os.path.join(os.getcwd(), dir_name)
    if sys.platform == "win32":
        os.popen("copy {0} {0}_copy".format(path))
    else:
        os.popen("cp {0} {0}_copy".format(path))
    print("File '{}' copied".format(path))


def remove_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    print("Are your sure? Y/N")
    agreement = input()
    if agreement == "Y" or "y" or "1":
        correct = True
    else:
        correct = False
    if correct:
        try:
            os.rmdir(dir_path)
            print("Directory '{}' was removed".format(dir_path))
        except OSError:
            print("Can`t remove directory")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "rm": remove_dir,
    "cd": normal.cd_f,
    "ls": normal.easy.ls_dirs,
    "cp": copy
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
