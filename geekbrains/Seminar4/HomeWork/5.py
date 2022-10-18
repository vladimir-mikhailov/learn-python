# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from numpy.polynomial import Polynomial as P
from numpy import polyadd


def get_polynome(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        polynome = P([int(s.split('.')[0])
                     for s in reversed(file.readline().split(' + '))])
    return polynome


p1 = get_polynome('manydick1.txt')
p2 = get_polynome('manydick2.txt')

with open('manydick_sum.txt', 'w', encoding='utf-8') as file:
    file.write(str(*polyadd(p1, p2)))
