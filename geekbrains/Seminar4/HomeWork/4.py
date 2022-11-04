# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:

# - k = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степепь многочлена: '))

coefficients = {i: randint(0, 10) for i in range(k + 1)}


def get_polynome(coefficients):  # функция будет переиспользована в 5 задаче
    lst = []
    for i in reversed(coefficients):
        if coefficients[i] != 0:
            if i == 0:
                lst.append(f'{coefficients[i]}')
            elif i == 1:
                lst.append(
                    f'{coefficients[i] if coefficients[i] != 1 else ""}x')
            elif i > 1:
                lst.append(
                    f'{coefficients[i] if coefficients[i] != 1 else ""}x^{i}')
    p = ' + '.join(lst)
    p += ' = 0'

    return p


# print('\n', get_polynome(coefficients), '\n')

with open('manydick.txt', 'w', encoding='utf-8') as file:
    file.write(get_polynome(coefficients))
