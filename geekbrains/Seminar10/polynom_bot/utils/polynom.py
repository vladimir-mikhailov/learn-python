# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def get_coefficients(message: str):
    '''
    Формирует словарь коэффициентов полинома из строки.
    Принимает многочлен вида: 9x^5 + 7x^4 + 7x^3 + 9x^2 + 6x + 17 = 0
    Возвращает словарь коэффициентов.
    '''
    coefficients = {}

    if '=' in message:
        message = message.split(' = ')[0]

    for e in reversed([x.split('^') for x in message.split(' + ')]):
        if len(e) == 1:
            if 'x' in str(e):
                coefficients[1] = int(e[0].replace('x', ''))
            else:
                coefficients[0] = int(e[0])
        else:
            coefficients[int(e[1])] = int(e[0].replace('x', ''))

    for i in reversed(range(max(coefficients.keys()) + 1)):
        if coefficients.get(i) is None:
            coefficients[i] = 0

    return coefficients


def sum_polynomes(coefficients):
    'Суммирует полиномы. Принимает и возвращает словари коэффициентов.'
    sum = {}
    for c in coefficients:
        for key in range(max(c.keys()) + 1):
            if sum.get(key) is not None:
                sum[key] += c.get(key)
            else:
                sum[key] = c[key]
    return sum


def get_polynome(coefficients):
    '''
    Собирает строковое представление полинома из списка коэффициентов.
    Возращает многочлен вида: 9x^5 + 7x^4 + 7x^3 + 9x^2 + 6x + 17 = 0
    '''
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


# p1 = get_coefficients(message)
# p2 = get_coefficients(message)
# p... = get_coefficients(message)
# sum = sum_polynomes(p1, p2)
# reply = get_polynome(sum)
