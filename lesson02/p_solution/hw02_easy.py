# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

def list2numlist(fruits_names):
    lenght = len(fruits_names)
    i = 0
    numlist = ''
    max_str_len = len(max(fruits_names)) # how add to string format?
    if lenght <= 0:
        return("Please enter fruits name")
    else:
        while lenght > i:
            numlist += "{}.{:>11} \n".format(i+1, fruits_names[i])
            i += 1
        return numlist

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def list_xor(list1, list2):
    for i in list2:
        list1.remove(i)
    return list1

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

def main():
    #Case 1
    fruits = ["apple", "banana", "kivi", "watermelon", "peach", "melon"]
    print(list2numlist(fruits))
    #Case 2
    a = [1,2,3,4,5,6,7,8,9]
    b = [2,4,6,8]
    print(list_xor(a,b))
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")