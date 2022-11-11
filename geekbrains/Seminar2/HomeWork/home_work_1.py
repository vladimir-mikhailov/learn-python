# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from re import subn
from decimal import Decimal

num = input('Введите число с плавающей точкой: ')

# Через Decimal.as_tuple:
print(sum(Decimal(num).as_tuple().digits))

# Через строку и str.replace():
print(sum(map(int, num.replace('-', '').replace('.', ''))))

# Через замену по RegExp
print(sum(map(int, subn('[-/.]', '', num)[0])))

# Через map
print(sum(map(int, (c for c in num if c.isdecimal()))))

# Через математику:
num = Decimal(num)

while int(num) != num:
    num *= 1

result = 0
while num:
    result += num % 10
    num //= 10
print(result)
