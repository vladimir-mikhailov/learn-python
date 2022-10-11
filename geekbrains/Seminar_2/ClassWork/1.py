# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# Пример:
# Для N = 5: 1, -3, 9, -27, 81

n = int(input('N = '))

result = []

for i in range(n):
    result.append((-3) ** i)

print(*result, sep=', ')

# Через итератор в одну строку:
print(*((-3) ** i for i in range(n)), sep=', ')
