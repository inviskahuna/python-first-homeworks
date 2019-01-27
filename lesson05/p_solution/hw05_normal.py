try:
    import lesson05.p_solution.hw05_easy as easy
except ModuleNotFoundError:
    import hw05_easy as easy

import os
import sys


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

class Menu:
    items = []

    def add_item(self, text, function):
        self.items.append({'text': text, 'func': function})

    def show(self):
        i = 1
        for t in self.items:
            print("{} {}".format(i, t['text']))
            i += 1

    def do(self, n):
        self.items[n]['func']()


def help_f():
    print('''We have this commands:
             "CD %PATH%" - Change directory by path like "C:\\Windows"
             "LS" - See current directory content
             "RMDIR %DIR_NAME%" - Remove directory
             "MKDIR %DIR_NAME%" - Make directory''')


def exit_f():
    print("Exit")
    sys.exit(0)


def cd_f():
    print("Please input dir")
    path = input()
    try:
        os.chdir(path)
        print("Now in '{}'".format(path))
    except OSError:
        print("Wrong path or not directory")


def mkdir_f():
    print("Please input dir name")
    name = input()
    try:
        os.mkdir(name)
        print("Directory '{}' was created".format(name))
    except OSError:
        print("Can`t create directory")


def rmdir_f():
    print("Please input dir name")
    name = input()
    print("Are your sure? Y/N")
    agreement: str = input()
    if agreement == "Y" or "y" or "1":
        correct = True
    else:
        correct = False
    if correct:
        try:
            os.rmdir(name)
            print("Directory '{}' was removed".format(name))
        except OSError:
            print("Can`t remove directory")


def my_file_manager():
    m = Menu()
    m.add_item("HELP", help_f)
    m.add_item("LS", easy.ls_dirs)
    m.add_item("CD", cd_f)
    m.add_item("RMDIR", rmdir_f)
    m.add_item("MKDIR", mkdir_f)
    m.add_item("EXIT", exit_f)
    while True:
        try:
            m.show()
            n = input("choice>")
            m.do(int(n) - 1)
        except ValueError:
            print("Wrong value, use nums for navigate")


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def main():
    my_file_manager()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
