# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from time import perf_counter

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
    start_time = perf_counter()

    result_iterator = [1]
    for i in range(1, n + 1):
        result_iterator.append(i * result_iterator[-1])

    finish_time = perf_counter()

    print(result_iterator[1:])
    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    # Через рекурсию:
    print('Через рекурсию:')
    start_time = perf_counter()

    def fact(num):
        if num in [0, 1]:
            return 1
        return num * fact(num - 1)
    result_rec = [fact(n) for n in range(1, n + 1)]

    finish_time = perf_counter()
    print(f'{result_rec}')

    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    # Через рекурсию с кэшем:
    print('Через рекурсию с кэшем:')
    start_time = perf_counter()

    def fact_cache(num, cache_lst):
        if num in [0, 1]:
            return 1
        if cache_lst[num - 1] != 0:
            return cache_lst[num - 1]
        cache_lst[num - 1] = num * fact_cache(num - 1, cache_lst)
        return cache_lst[num - 1]

    cache_lst = [0 for i in range(n)]
    result_rec_cache = [fact_cache(n, cache_lst) for n in range(1, n + 1)]

    finish_time = perf_counter()
    print(f'{result_rec_cache}')

    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    # Через лямбду
    # factorial = lambda x: x if x == 1 else x * factorial(x - 1)
    # print([factorial(i) for i in range(1, n + 1)])

    # тоже самое но без лямбды:
    print('Короткая запись с лямбдой али без:')
    start_time = perf_counter()

    def factorial(x):
        return x if x == 1 else x * factorial(x - 1)

    fact_list = [factorial(i) for i in range(1, n + 1)]

    finish_time = perf_counter()
    print(fact_list)
    print(f'Выполнено за {(finish_time - start_time):0.8f} секунд\n')

    # Через функцию-генератор с yield (дописать)

    # def fact_gen(n):
    #     last = 1
    #     for i in range(1, n):
    #         i *= i + 1
    #         yield last
