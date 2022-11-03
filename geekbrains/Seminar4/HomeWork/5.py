# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def get_coefficients(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        coefficients = {}
        for e in reversed([x.split('^')
                           for x in file.readline().split(' = ')[0].split(' + ')]):
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


def sum_polynomes(*coefficients):
    sum = {}
    for c in coefficients:
        for i in range(max(c.keys()) + 1):
            if sum.get(i) is not None:
                sum[i] += c.get(i)
            else:
                sum[i] = c[i]
    return sum


def get_polynome(coefficients):
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


p1 = get_coefficients('manydick1.txt')
p2 = get_coefficients('manydick2.txt')
sum = sum_polynomes(p1, p2)

# print(get_polynome(p1))
# print('+')
# print(get_polynome(p2))
# print('=')
# print(get_polynome(sum))

with open('manydick_sum.txt', 'w', encoding='utf-8') as file:
    file.write(get_polynome(sum))
