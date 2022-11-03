# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd, lcm

a = int(input('A = '))
b = int(input('B = '))

# Через цикл
nok = max(a, b)
min_num = min(a, b)

while nok % min_num:
    nok *= min_num

print('НОК:', nok)

# Через наибольший общий делитель
print('НОК:', int(a * b / gcd(a, b)))

# Через math.lcm
print('НОК:', lcm(a, b))

# Через рекурсию


def gcd_rec(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)


print('НОК:', int(a * b / gcd_rec(a, b)))
