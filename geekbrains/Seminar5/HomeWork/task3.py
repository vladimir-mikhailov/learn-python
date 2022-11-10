# Создайте программу для игры в "Крестики-нолики".

import os
import platform
from random import randint


# field_map_indices = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
field_map = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
field = [['•', '•', '•'], ['•', '•', '•'], ['•', '•', '•']]

# Случайное распределение первого хода и крестика/нолика
players = set(['Игрок', 'Компьютер'])


def print_field(field):
    for line in field:
        print(*line)


def get_coord(player):
    free_fields = get_free_fields()

    if player == 'Игрок':
        while True:
            try:
                num = translate_to_coord(int(input('\nВведите поле:')))
                if num in free_fields:
                    return num
                print('Введите номер свободного поля от 1 до 9. Попробуйте ещё.\n')
            except ValueError:
                print('Введена не цифра. Попробуйте ещё.\n')

    return free_fields[randint(0, len(free_fields) - 1)]


def translate_to_coord(num):
    match num:
        case 1:
            return [0, 0]
        case 2:
            return [0, 1]
        case 3:
            return [0, 2]
        case 4:
            return [1, 0]
        case 5:
            return [1, 1]
        case 6:
            return [1, 2]
        case 7:
            return [2, 0]
        case 8:
            return [2, 1]
        case 9:
            return [2, 2]
        case _:
            print('Введите число от 1 до 9 (см. карту поля)')


def print_fields(field, field_map_num):
    clear()
    print('Карта игрового поля:')
    print_field(field_map_num)

    print('Игровое поле:')
    print_field(field)


def turn(coord, field, mark, player):
    field[coord[0]][coord[1]] = mark
    print_fields(field, field_map)
    print('Platform:', platform.system())


def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        return os.system('clear')
    elif platform.system() == "Windows":
        return os.system('cls')


def check_win(coord, field, mark):
    # Горизонталь
    x = coord[0]
    hor = field[x][0:3]

    # Вертикаль
    y = coord[1]
    vert = [field[c][y] for c in range(3)]

    # Диагональ1
    diag1 = [field[x][x] for x in range(3)]

    # Диагональ2
    y = 0
    diag2 = [field[x][abs(x-2)] for x in range(3)]

    for p in [hor, vert, diag1, diag2]:
        if p.count(mark) == 3:
            return True

    return False


def get_free_fields():
    free_fields = []
    for x in range(3):
        for y in range(3):
            if field[x][y] == '•':
                free_fields.append([x, y])
    return free_fields


print_fields(field, field_map)

while True:
    game_over = False
    for player in players:
        mark = '0'
        if player == 'Игрок':
            mark = 'X'
        coord = get_coord(player)
        turn(coord, field, mark, player)
        if check_win(coord, field, mark):
            print(f'{player} играл за {mark} и выиграл.')
            game_over = True
            break
        if len(get_free_fields()) == 0:
            print('Ничья')
            game_over = True
            break
    if game_over:
        break
