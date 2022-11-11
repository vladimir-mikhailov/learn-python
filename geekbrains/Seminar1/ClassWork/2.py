# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))

numbers = [a, b, c, d, e]

# for i in range(0, 6):
#     numbers[i] = int(input(f'Введите {i + 1}-е число: '))

maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print(maximum)
