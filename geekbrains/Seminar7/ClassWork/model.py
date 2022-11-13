# Бэкенд, Функции для работы с данными
x = 0
y = 0


def init(a, b):
    global x
    global y
    x = int(a)
    y = int(b)


def multiply():
    return x * y


def sum():
    return x + y


def divide():
    return x / y


def sub():
    return x - y
