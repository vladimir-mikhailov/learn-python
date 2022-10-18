# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10 ^ {-1} ≤ d ≤10 ^ {-10}$

from math import acos, pi

# d = int(input('Точность, цифр после запятой: '))
d = len((input('Точность в формате 0.001: ')).split('.')[1])

print('Pi через math.acos =', round(2 * acos(0.0), d))

print('Pi через math.pi   =', round(pi, d))
