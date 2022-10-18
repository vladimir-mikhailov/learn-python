# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:

# - k = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

from numpy.polynomial import Polynomial as P

k = int(input('Введите натуральную степепь многочлена: '))

coefficients = [randint(0, 100) for i in range(k + 1)]

p = ' + '.join(reversed(str(P(coefficients)).replace('·',
               '*').replace('.0', '').split(' + ')))

with open('manydick.txt', 'w', encoding='utf-8') as file:
    file.write(f'k = {k} => {p} = 0')
