# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

lines = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = 2

print(any(filter(lambda x: str(num) in x, lines)))

print(str(num) in ' '.join(lines))
