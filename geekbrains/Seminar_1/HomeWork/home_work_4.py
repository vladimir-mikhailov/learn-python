# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    try:
        quarter = int(
            input('Введите номер четверти или любую другую цифру для выхода: '))
    except ValueError:
        print('Неправильный ввод')

    match quarter:
        case 1:
            print('x > 0, y > 0')
        case 2:
            print('x < 0, y > 0')
        case 3:
            print('x < 0, y < 0')
        case 4:
            print('x > 0, y < 0')
        case _:
            print('Что-то не то')
            break
