import os
from re import search
from sys import platform

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dirs():
    dirs = 0
    names = ['dir_' + str(i) for i in range(9)]
    for i in names:
        os.mkdir(i)
        dirs += 1
    return "{} dirs make".format(dirs)


def remove_dirs():
    dirs = 0
    for i in os.listdir():
        if search('dir+', i):
            os.rmdir(i)
            dirs += 1
    return "{} dirs removed".format(dirs)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def ls_dirs():
    directory = os.listdir()
    print(tuple(directory))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_myself():
    path = os.path.realpath(__file__)
    if platform == "win32":
        os.popen("copy {0} {0}_copy".format(path))
    else:
        os.popen("cp {0} {0}_copy".format(path))
    return "File \"{}\" was copied".format(path)


def main():
    print(make_dirs())
    ls_dirs()
    print(remove_dirs())
    print(copy_myself())
    print(ls_dirs())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
