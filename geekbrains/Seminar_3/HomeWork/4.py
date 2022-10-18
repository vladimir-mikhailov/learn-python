# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_binary(n):
    bin_n = ''
    while n // 2 > 0:
        bin_n = str(n % 2) + bin_n
        n //= 2
    bin_n = str(n) + bin_n
    return bin_n


while True:
    try:
        n = int(input('N = '))
        print(f'{n} -> {to_binary(n)}')
    except ValueError:
        print('Good Bye!')
        break
