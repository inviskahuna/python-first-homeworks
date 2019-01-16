
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
    floor = 0
    apartaments_m = 0
    i = 1
    while(apartaments_m < apartaments_num):
        apartaments_m += i**2
        floor += 1
    t = floor
    if(apartaments_m != apartaments_num):
        while(apartaments_m > apartaments_num):
            apartaments_m -= i
    return apartaments_num, t, 


def main():
    linean(equation, 2.5)
    date = '26.11.2019'
    print(iscorrectdate(date))
    print(crazy_tower_lift(4))
    test(13)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")