# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def quadratic_list(in_list):
    return [x**2 for x in in_list]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


def fruits_lists(fruits1, fruits2):
    return [x for x in fruits1 if x in fruits2]

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def condition_list(in_list):
    return [x for x in in_list if (x % 3 == 0) and (x % 4 != 0) and (x > 0)]


def main():
    q_list = [1, 2, 4, 0]
    print(quadratic_list(q_list))
    fr1 = ["melon", "apple", "watermelon", "kiwi"]
    fr2 = ["apple", "banana", "peach", "kiwi"]
    print(fruits_lists(fr1, fr2))
    print(condition_list(range(-10, 40)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
