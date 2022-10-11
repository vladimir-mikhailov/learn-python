# 4. Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

try:
    file = open('file.txt', 'r', encoding='utf-8')
    lines = file.readlines()

    while len(lines) > 0:
        try:
            n = int(
                input('Введите целое число N (или что-то другое, чтобы выйти): '))
        except ValueError:
            print('Good Bye!')
            break

        range_n = [randint(-n, n) for i in range(n - 1)]

        products = {}

        for line in lines:
            try:
                i = int(line)
                products[i] = range_n[i]
            except ValueError:
                print(f'\nНевозможно спарсить {line}')
            except IndexError:
                print(
                    f'Элемента с индексом {i} не существует (от 0 до {len(range_n) - 1})')

        print(f'\nЗначения элементов на указанных позициях: {products}\n')

        if len(products) > 0:
            product = 1
            for value in products.values():
                product *= value

            print(f'Произведение значений: {product}\n')

    else:
        print('Файл пустой')

except FileNotFoundError:
    print('Файла не существует')
