# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def sum_odds(n):
    lst = [randint(1, 10) for i in range(n)]
    odds = [lst[i] for i in range(1, n, 2)]
    print(f'{lst} -> на нечётных позициях элементы {" и ".join(map(str, odds))}. Сумма: {sum(odds)}')


while True:
    try:
        n = input('\nВведите длину списка или что угодно для выхода: ')
        n = int(n)
        print()
        sum_odds(n)
    except ValueError:
        print('\nGood Bye!\n')
        break
