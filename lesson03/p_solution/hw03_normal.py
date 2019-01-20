from random import choice
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a = 0
    b = 1
    c = []
# like a dynamic prog
    for __ in range(m):
        a, b = b, a + b
        c.append(a)
    return c[n:]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    # Reference: http://www.itmathrepetitor.ru/sortirovka-khoara-bystraya-sortirovka/
    if len(origin_list) <= 1:
        return origin_list
    else:
        seed = choice(origin_list)
    l_nums = [n for n in origin_list if n < seed]
    e_nums = [seed] * origin_list.count(seed)
    b_nums = [n for n in origin_list if n > seed]
    return sort_to_max(l_nums) + e_nums + sort_to_max(b_nums)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def main():
    print(fibonacci(4, 32))
    print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
