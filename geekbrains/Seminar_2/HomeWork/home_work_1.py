# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from re import subn
from functools import reduce
from decimal import Decimal

num = input('Введите число с плавающей точкой: ')

# Через Decimal.as_tuple:
print(reduce(lambda x, y: x + y, Decimal(num).as_tuple().digits))

# Через строку и str.replace():
print(reduce(lambda x, y: int(x) + int(y), num.replace('-', '').replace('.', '')))

# Через замену по RegExp
print(reduce(lambda x, y: int(x) + int(y), subn('[-/.]', '', num)[0]))
