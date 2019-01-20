import re
import os


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def my_calc(in_str: str):
    pattern = r'((\d+) (\d+/\d+) ([+,-]) (\d+) (\d+/\d+))'
    #         numr
    # integer-------
    #         denumr
    if re.match(pattern, in_str):
        parser = re.split('\D+', in_str)
        parser = list(map(int, parser))
        integerA = parser[0]
        numrA = parser[1]
        denumrA = parser[2]
        numrA += denumrA*integerA
        integerB = parser[3]
        numrB = parser[4]
        denumrB = parser[5]
        numrB += denumrB * integerB

        denumr = denumrA * denumrB
        numrA *= denumrB
        numrB *= denumrA
        numr = numrA + numrB

        d_out = denumr
        n_out = numr % denumr
        i_out = (numr - n_out)/ denumr

        ret = int(i_out), n_out, d_out
    else:
        ret = ("bad format use X A./B +- Y C/D")
    return ret

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def salary():

    def make_dict(w, h):
        lw = []
        lh = []
        for i in w:
            workers_dict = {"name": i[0], "l_name": i[1], "wage": i[2], "prof": i[3], "norm": i[4]}
            lw.append(workers_dict)
        for i in h:
            hours_dict = {"name": i[0], "l_name": i[1], "hours": i[2]}
            lh.append(hours_dict)
        return lw, lh

    def calc_salary(wage, norm, hours):
        wage = int(wage)
        norm = int(norm)
        hours = int(hours)
        if hours <= norm:
            m_salary = wage * (hours / norm)
        else:
            e_hours = (hours - norm) * 2
            m_salary = wage * (1 + (e_hours / norm))
        return round(m_salary, 2)

    workers = os.path.join("data", "workers")
    hours_of = os.path.join("data", "hours_of")

    pattern_w = r'(\w+\s+\w+\s+\d+\s+\w+\s+\d+)'
    pattern_h = r'(\w+\s+\w+\s+\d+)'
    workers_list = []
    hours_list = []
    # Read workers
    with open(workers, 'r', encoding="UTF8-") as f:
        r = re.findall(pattern_w, f.read())
        for i in r:
            workers_list.append(re.split("\s+", i))
    # Read hours
    with open(hours_of, 'r', encoding="UTF8-") as f:
        r = re.findall(pattern_h, f.read())
        for i in r:
            hours_list.append(re.split("\s+", i))

        dictionares = make_dict(workers_list, hours_list)
        w_dict = dictionares[0]
        h_dict = dictionares[1]
        i = 0
        sss = []
        while i < len(w_dict):
            sss.append({w_dict[i]["name"], w_dict[i]["l_name"], calc_salary(w_dict[i]['wage'], w_dict[i]['norm'], h_dict[i]["hours"])})
            i += 1
        return sss


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def main():
    print(my_calc("1 1/3 + 0 2/5"))
    print(salary())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
