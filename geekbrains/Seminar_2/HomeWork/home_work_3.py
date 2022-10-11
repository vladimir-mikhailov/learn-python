# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

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
    print('Через for:')
    start_time = time()

    result = [2]
    for i in range(2, n + 1):
        result.append(result[i - 2] + (1 + 1 / i) ** i)
    finish_time = time()

    for i in range(n):
        print(f'{i + 1} -> {result[i]}')
    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    print('Через рекурсию:')
    start_time = time()

    def rec(num):
        if num == 0:
            return 0
        return rec(num - 1) + (1 + 1 / num) ** num
    result_rec = [rec(i) for i in range(1, n + 1)]

    finish_time = time()
    for i in range(n):
        print(f'{i + 1} -> {result_rec[i]}')
    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')
