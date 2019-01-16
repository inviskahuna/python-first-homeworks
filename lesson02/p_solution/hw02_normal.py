from math import sqrt
from datetime import date
from random import randint
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def num_sqrts(num_list):
    ret = []
    for i in num_list:
        if i > 0:
            t = sqrt(i)
            if(t % 1 > 1e-6): #For float round error
               pass #print("{:1.4} is float sqrt".format(t))
            else:
                ret.append(int(t))
        pass
    return ret

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

def numdat2strdat(numd):
    #maybe can use num2words thirdparty library, now hardway with stdlib
    d = str(numd).split('.')
    di = []
    for i in d:
        di.append(int(i))
    dd = date(int(di[2]),int(di[1]),int(di[0]))
    A = (dd.strftime("It`s %B %dth %Y")) #Beuty
    days = {"01":"first", "02":"second", "03":"third", "04":"fours", "05":"fifth",
            "06":"sixth", "07":"seventh", "08":"eighth", "09":"nineth", "10":"tenth",
            "11":"eleven", "12":"twelve", "13":"thirteenth", "14":"second", "15":"third",
            "16":"sixteenth", "17":"seventeenth", "18":"eighteenth", "19":"nineteenth", "20":"twenty",
            "21":"twenty one", "22":"twenty two", "23":"twenty three", "24":"twenty four", "25":"twenty five",
            "26":"twenty six", "27":"twenty seven", "28":"twenty eight", "29":"twenty nine", "30":"thirty",
            "31":"thirty one"}
    B = (dd.strftime("It`s %B the {}, %Y").format(days[d[0]])) # ugly
    return A, B

        

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def fill_randoms(size_n):
    l = []
    i = 0
    while i <= size_n:
        l.append(randint(-100, 100))
        i += 1
    return l

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def main():
    #------------------------------#
    nums = [2, -5, 8, 9, -25, 25, 4]
    print(num_sqrts(nums))
    #------------------------------#
    data = "16.04.2013"
    print(numdat2strdat(data))
    #------------------------------#
    print(fill_randoms(100))
    #------------------------------#

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")