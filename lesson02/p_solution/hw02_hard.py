
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

def linean(equation_str, input_x):
    raw = str(equation_str)
    x = float(input_x)
    splited = raw.split(" ")
    k = float(str(splited[2]).replace('x', ""))
    b = float(splited[4])
    if(splited[3] == '+'):
        s = 1
    elif(splited[3] == '-'):
        s = -1
    else:
        print("error")
    y = k*x+(b*s)
    print("y = {}x + {}".format(k, b))

    print("If x={}, then y={}".format(x, y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def iscorrectdate(input_date):
    date = str(input_date)
    list_date = date.split('.')
    dd = list_date[0]
    mm = list_date[1]
    yyyy = list_date[2]
    if len(dd) == 2 and len(mm) ==2 and len(yyyy) == 4:
        dd = int(dd)
        mm = int(mm)
        yyyy = int(yyyy)
        if(dd > 0 and dd <= 31):
            ret1 = True
        else:
            return "Incorrect day"
        if(mm > 0 and mm <= 12):
            ret2 = True
        else:
            return "Incorrect month"
        if(yyyy > 0 and yyyy <= 9999):
            ret3 = True
        else:
            return "Incorrect year"
    else:
        return "Incorrect input date str lenght"
        
    if(ret1 and ret2 and ret3):
            return "Date is correct"

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
def crazy_tower_lift(apartaments_num):
    #I`m use refrence https://geekbrains.ru/posts/babylon_task & 
    #                 https://fido7.ru.algorithms.narkive.com/r6fkHksY
    block = 0   
    last_flat = 0   
    last_floor = 0 
    i = 0
    while apartaments_num > last_flat:
        block += 1
        last_flat += block * block
        last_floor += block
    while last_flat > apartaments_num:
        last_flat -= 1
        if i < block - 1:
            i += 1
        else:
            last_floor -= 1
            i = 0
    position = block - i
    return('Floor: {} Apartaments: {}'.format(last_floor, position))


def main():
    print("#------------------------------#")
    print("CASE 1")
    linean(equation, 2.5)
    print("#------------------------------#")
    print("CASE 2")
    date = '26.11.2019'
    print(iscorrectdate(date))
    print("#------------------------------#")
    print("CASE 3")
    print(crazy_tower_lift(250005))
    print("#------------------------------#")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")