# 5. Реализуйте алгоритм перемешивания списка

from random import randint

while True:
    try:
        length = int(
            input('Введите длину списка случайных чисел (или 0, чтобы выйти): '))
    except ValueError:
        print('Введите целое число или 0, чтобы завершить.')

    if length == 0:
        print('Good Bye!')
        break

    lst = [randint(0, 101) for i in range(length)]

    random_indices = set([])
    while len(random_indices) < length:
        random_indices.add(str(randint(0, length - 1)))

    sorted_list = [lst[int(i)] for i in random_indices]

    print(f'Исходный список:     {lst}')
    print(f'Перемешанный список: {sorted_list}')
