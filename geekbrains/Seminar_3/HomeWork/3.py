# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint

n = int(input('Длина списка: '))

lst = [str(randint(0, 1000) / 100) for i in range(n)]

afterpoints = [round(float(el) - float(el.split('.')[0]), 2) for el in lst]

print(f'{lst} -> {max(afterpoints) - min(afterpoints)}')
