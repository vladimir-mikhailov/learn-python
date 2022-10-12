# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from time import time

print()
while True:
    try:
        n = int(
            input('Введите целое число (или любой символ, чтобы выйти): '))
    except ValueError:
        print('Введено не целое число. Goodbye!')
        break

    print()

    # Через цикл for:
    print('Через for:')
    start_time = time()

    result_iterator = [1]
    for i in range(1, n + 1):
        result_iterator.append(i * result_iterator[i - 1])

    finish_time = time()

    print(result_iterator[1:])
    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    # Через рекурсию:
    print('Через рекурсию:')
    start_time = time()

    def fact(num):
        if num in [0, 1]:
            return 1
        return num * fact(num - 1)
    result_rec = [fact(n) for n in range(1, n + 1)]

    finish_time = time()
    print(f'{result_rec}')

    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')
