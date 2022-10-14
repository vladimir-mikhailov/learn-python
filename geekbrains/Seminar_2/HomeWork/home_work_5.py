# 5. Реализуйте алгоритм перемешивания списка

from random import randint, shuffle

while True:
    try:
        length = int(
            input('Введите длину списка случайных чисел (или любой символ, чтобы выйти): '))
    except ValueError:
        print('Good Bye!')
        break

    if length == 0:
        print('Good Bye!')
        break

    lst = [randint(0, 101) for i in range(length)]
    print(f'Исходный список:      {lst}')

    for i in range(length):
        rnd = randint(0, length - 1)
        lst[i], lst[rnd] = lst[rnd], lst[i]

    print(f'Перемешанный список : {lst}')

    # Через random.shuffle
    shuffle(lst)
    print(f'Перемешанный шаффлом: {lst}')
