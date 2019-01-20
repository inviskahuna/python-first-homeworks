# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number: float, ndigits: int):
    e = number * 10**ndigits
    r = (e - int(e)) * 10
    if r >= 5:
        e = int(e + 1)
    return e / 10 ** ndigits


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number: int):
    ticket_list = list(str(ticket_number))
    num_list = list(map(int, ticket_list))
    ticket_len = len(num_list)
    if (ticket_len != 6):
        raise Exception("Ticket length must equal six")
    else:
        left = sum(num_list[0:3])
        right = sum(num_list[3:6])
        return "You have a lucky ticket -> {}".format(ticket_number) if left == right else "You loose"


def main():
    print("#------------------------------#")
    print("CASE 1")
    print(my_round(2.1234567, 5))
    print(my_round(2.1991117, 5))
    print(my_round(2.4567890, 5))
    print(my_round(200.9993267, 5))
    print(my_round(1.133323347, 5))
    print(my_round(-10.9999967, 3))
    print("#------------------------------#")
    print("CASE 2")
    print(lucky_ticket(123006))
    print(lucky_ticket(123321))
    print(lucky_ticket(123020))
    print(lucky_ticket(436751))
    print("#------------------------------#")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exit")
