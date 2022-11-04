# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Натуральное число: '))

i = 2
multipliers = set([])
while i * i <= n:
    while n % i == 0:
        multipliers.add(i)
        n //= i
    i += 1
if n != 1:
    multipliers.add(n)

print(multipliers)
