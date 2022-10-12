# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

from time import perf_counter

while True:
    try:
        n = int(
            input('\nВведите целое число (или любой символ, чтобы выйти): '))
    except ValueError:
        print('Введено не целое число. Goodbye!')
        break

    print()

    # Через цикл for:
    print('Через for:\n')
    start_time = perf_counter()

    result = []
    for i in range(1, n + 1):
        result.append((0 if i == 1 else result[i - 2]) + (1 + 1 / i) ** i)
    finish_time = perf_counter()
    time_for = finish_time - start_time

    for i in range(n):
        print(f'{i + 1} -> {result[i]}')
    print(f'\nВыполнено за {time_for:0.8f} секунд\n')

    # Через рекурсию с кэшем:
    print('Через рекурсию с кэшированием:\n')
    start_time = perf_counter()

    def rec(num, cache):
        if num == 0:
            return 0
        if cache[num - 1] != 0:
            return cache[num - 1]
        cache[num - 1] = rec(num - 1, cache) + (1 + 1 / num) ** num
        return cache[num - 1]

    cache = [0 for i in range(n)]
    result_rec = [rec(i + 1, cache) for i in reversed(range(n))]
    result_rec.reverse()

    finish_time = perf_counter()
    time_rec = finish_time - start_time

    print()
    for i in range(n):
        print(f'{i + 1} -> {result_rec[i]}')
    print(f'\nВыполнено за {time_rec:0.8f} секунд\n')

    # Через рекурсию без кэширования:
    print('Через рекурсию без кэширования:\n')
    start_time = perf_counter()

    def rec_no_cache(num):
        if num == 0:
            return 0
        return rec_no_cache(num - 1) + (1 + 1 / num) ** num

    result_rec_no_cache = [rec_no_cache(i + 1) for i in reversed(range(n))]
    result_rec_no_cache.reverse()

    finish_time = perf_counter()
    time_rec_no_cache = finish_time - start_time
    print()
    for i in range(n):
        print(f'{i + 1} -> {result_rec_no_cache[i]}')
    print(f'\nВыполнено за {time_rec_no_cache:0.8f} секунд\n')

    print(f'\nОбщая сводка по скорости для N = {n}:\n')
    print(f'Через цикл for:    {time_for:0.8f} сек')
    print(f'Рекурсия с кэшем:  {time_rec:0.8f} сек')
    print(f'Рекурсия без кэша: {time_rec_no_cache:0.8f} сек')
