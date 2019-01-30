# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
from functools import reduce


class Line(object):
    def __init__(self, in_a, in_b):
        self.a = in_a[0]
        self.b = in_b[0]

    def calc_len(self):
        a = self.a
        b = self.b
        return sqrt((a[0]-b[0]) ** 2 + (a[1] - b[1]) ** 2)  # TODO: fix work with negative value


class Triangle(object):
    # -----[b]-----
    # -----*-*-----
    # ----*---*----
    # ---*-----*---
    # -[a]*****[c]-
    coords = {"a": [], "b": [], "c": []}

    def __init__(self, coords_list: list):  # Type like this [[0,0],[1,1],[2,2]]
        self.coords.get("a").append(coords_list[0])
        self.coords.get("b").append(coords_list[1])
        self.coords.get("c").append(coords_list[2])

    def calc_height(self):
        line_ab = Line(self.coords.get("a"), self.coords.get("b"))
        line_bc = Line(self.coords.get("b"), self.coords.get("c"))
        line_ca = Line(self.coords.get("c"), self.coords.get("a"))
        lengths = [line_ab.calc_len(), line_bc.calc_len(), line_ca.calc_len()]
        p = reduce(lambda x, y: x + y, lengths) / 2
        return 2 * sqrt(p * (p - lengths[0]) * (p - lengths[1]) * (p - lengths[2]))/lengths[1]

    def calc_area(self):
        base = Line(self.coords.get("c"), self.coords.get("a"))
        return (base.calc_len()/2) / self.calc_height()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezium(object):
    # ------(b)********(c)------
    # ------*------------*------
    # -----*--------------*-----
    # ---(a)***************(d)--
    coords = {"a": [], "b": [], "c": [], "d": []}

    def __init__(self, coords_list: list):  # Type like this [[0,0],[1,1],[2,2]]
        self.coords.get("a").append(coords_list[0])
        self.coords.get("b").append(coords_list[1])
        self.coords.get("c").append(coords_list[2])
        self.coords.get("d").append(coords_list[2])

    def perimeter(self, need_lengths=False):
        line_ab = Line(self.coords.get("a"), self.coords.get("b"))
        line_bc = Line(self.coords.get("b"), self.coords.get("c"))
        line_cd = Line(self.coords.get("c"), self.coords.get("d"))
        line_da = Line(self.coords.get("d"), self.coords.get("a"))
        lengths = [line_ab.calc_len(), line_bc.calc_len(), line_cd.calc_len(), line_da.calc_len()]
        p = reduce(lambda x, y: x + y, lengths)
        return lengths if need_lengths else p

    def area(self):
        lengths = self.perimeter(need_lengths=True)
        a = lengths[3]
        b = lengths[1]
        return (a + b)/2 * sqrt((lengths[0] * lengths[2]) - ((a - b)/4))

    def is_isosceles(self):
        lengths = self.perimeter(need_lengths=True)
        return lengths[0] == lengths[2]


def main():
    triangle = Triangle([[0, 0], [9, 5], [14, 3]])
    trapezium = Trapezium([[2, 4], [0, 2], [0, 7], [2, 5]])
    print(triangle.calc_height())
    print(triangle.calc_area())
    print(trapezium.perimeter())
    print(trapezium.area())
    print(trapezium.is_isosceles())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
