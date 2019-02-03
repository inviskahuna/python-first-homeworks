#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card(object):

    @staticmethod
    def split_list(input_list: list, wanted_parts=1):
        length = len(input_list)
        return [input_list[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    @staticmethod
    def sort_rows(row: list):
        indexes = []
        values = []
        sorted_row = [0]*9
        for index, value in enumerate(row):
            if value != 0:
                indexes.append(index)
                values.append(value)
        sorted_values = sorted(values)
        for j, i in enumerate(indexes):
            sorted_row[i] = sorted_values[j]
        return sorted_row

    def make_card(self):
        card = []
        for _ in range(0, 3):
            row_sample = (random.sample(range(1, 91), 5)) + [0]*4
            random.shuffle(row_sample)
            card.append(self.sort_rows(row_sample))
        return card

    @staticmethod
    def verbose_card(card_array: list):
        verbose = "_"*55 + "\n"
        for i in card_array:
            verbose += "|"
            for j in i:
                if j != 0:
                    verbose += ("{:4} |").format(j)
                else:
                    verbose += ("{:4} |").format("  ")
            verbose += ("\r\n")
        verbose += "-" * 55
        return verbose

def main():
    c = Card()
    a = c.make_card()
    print(c.verbose_card(a))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
