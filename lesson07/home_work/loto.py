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
import time


class Card(object):
    card = []

    def __init__(self):
        self.card = []
        for _ in range(0, 3):
            row_sample = (random.sample(range(1, 91), 5)) + [0] * 4
            random.shuffle(row_sample)
            self.card.append(self.sort_rows(row_sample))

    def __str__(self):
        return self.verbose_card()

    @staticmethod
    def split_list(input_list: list, wanted_parts=1):
        length = len(input_list)
        return [input_list[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    @staticmethod
    def sort_rows(row: list):
        indexes = []
        values = []
        sorted_row = [0] * 9
        for index, value in enumerate(row):
            if value != 0:
                indexes.append(index)
                values.append(value)
        sorted_values = sorted(values)
        for j, i in enumerate(indexes):
            sorted_row[i] = sorted_values[j]
        return sorted_row

    def card_array(self):
        card = []
        for _ in range(0, 3):
            row_sample = (random.sample(range(1, 91), 5)) + [0] * 4
            random.shuffle(row_sample)
            card.append(self.sort_rows(row_sample))
        return card

    def verbose_card(self):
        verbose = "_" * 55 + "\n"
        for i in self.card:
            verbose += "|"
            for j in i:
                if j != 0:
                    verbose += ("{:4} |").format(j)
                else:
                    verbose += ("{:4} |").format("  ")
            verbose += ("\r\n")
        verbose += "-" * 55
        return verbose


class Game(Card):
    barrels_in_bag = 90
    bag = random.sample(range(1, 91), 90)

    def __init__(self):
        self.player = Card()
        self.pc = Card()
        print(f'''Да начнется игра между ПК и человеком! 
        90 бочонков в мешке, по одной карточке каждому''')
        print("PC\n", self.pc, "\nPlayer", "\n", self.player)

    def get_barrel(self):
        random.shuffle(self.bag)  # перемещаем бочонки в мешке
        return self.bag.pop(0)  # выдадаим первый попавшийся бочонок и удалим его из мешка

    def find_in_card(self, card: list, barrel: int):
        row = 0
        for i in card:
            row += 1
            column = 0
            for j in i:
                column += 1
                if j == barrel:
                    return row, column

    def crossout_card_coord(self, card, c: tuple):
        x = c[0] - 1
        y = c[1] - 1
        # print(f"X{x}, Y{y}")
        print(card[x][y])
        card[x][y] = " X"

    def calc_points(self, card):
        points = 0
        for i in card:
            for j in i:
                if j == " X":
                    points += 1
        return points


def main():
    g = Game()
    for _ in range(0, 90):
        barrel = g.get_barrel()
        player_match = g.find_in_card(g.player.card, barrel)
        pc_match = g.find_in_card(g.pc.card, barrel)

        print(f"Вытащили бочонок {barrel}")
        print(f"Есть ли в вашей карточке? [1 - да, зачеркнуть], [0 - нет, продолжить]")
        inp = input()

        player_choise = False if int(inp) == 0 else True
        print(f"Inp = {inp}, choise = {player_choise}, player match = {player_match}, pc mathc = {pc_match}")
        if pc_match is not None:
            g.crossout_card_coord(g.pc.card, pc_match)

        if player_match is not None:
            if player_choise:
                print("ОК")
                g.crossout_card_coord(g.player.card, player_match)
            else:
                print("А он есть")
        elif player_match is None:
            if player_choise:
                print("Конец игры. Вы потеряли внимательность!")
                time.sleep(10)
                return
            else:
                print("Ок")
        print(f"ПК:\n{g.pc}\nИгрок\n{g.player}")
        print(f"{len(g.bag)} в мешке")
        pc_points = g.calc_points(g.pc.card)
        player_points = g.calc_points(g.player.card)
        if pc_points == 15:
            print("Победил ПК")
            time.sleep(10)
            return
        elif player_points == 15:
            print("Победил Игрок")
            time.sleep(10)
            return
        else:
            print(f"Игра продолжается ПК = {pc_points}, Player = {player_points}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
