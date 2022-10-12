# 4. Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    print()
    while len(lines) > 0:
        try:
            n = int(
                input('Введите целое число N (или что-то другое, чтобы выйти): '))
        except ValueError:
            print('Good Bye!')
            break

        random_values = [randint(-n, n) for i in range(n)]
        print()
        positions_and_values = {}

        for line in lines:
            try:
                i = int(line)
                positions_and_values[i] = random_values[i]
            except ValueError:
                print(f'\nНевозможно спарсить {line}')
            except IndexError:
                print(
                    f'Элемента с индексом {i} не существует (от 0 до {len(random_values) - 1})')

        print(
            f'\nЗначения элементов на указанных позициях: {positions_and_values}\n')

        if len(positions_and_values) > 0:
            product = 1
            for value in positions_and_values.values():
                product *= value

            print(f'Произведение значений: {product}\n')

    else:
        print('Файл пустой')

except FileNotFoundError:
    print('Файла не существует')
