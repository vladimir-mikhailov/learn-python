# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

pot = 56
max_take = 28

rest_in_pot = pot


def get_quantity(player, pot, rest_in_pot, max_take):
    if player == 'Игрок':
        while True:
            try:
                num = int(input('Сколько берёте? '))
                if check_quantity(num, pot, max_take):
                    return num
            except ValueError:
                print('Введена не цифра. Попробуйте ещё.\n')

    elif player == 'Глупый компьютер':
        return randint(1, min(max_take + 1, rest_in_pot + 1))

    # Хитрый компьютер:
    if rest_in_pot > max_take:
        if rest_in_pot % max_take - 1 == 0:
            return max_take
        elif rest_in_pot % max_take - 1 > 0:
            return rest_in_pot % max_take - 1
        else:
            return max_take - 1
    else:
        return min(max_take, rest_in_pot)


def check_quantity(num, pot, max_take):
    if num <= 0:
        print('Вы должны взять хотя бы одну конфету.')
        return False
    elif num > max_take:
        print(f'Можно брать не более {max_take} конфет.')
        return False
    elif num > pot:
        print(f'Осталось только {pot} конфет.')
        return False
    return True


computer = 'Хитрый компьютер' if input(
    'Выберите сложность соперника:\n'
    '1 - Легко\n'
    '2 - Сложно\n'
    'Ваш выбор: '


) == '2' else 'Глупый компьютер'

# Жеребьёвка через встроенную случайную сортировку set:
players = {'Игрок', computer}

print(
    f'\nИгра началась. В банке: {pot} конфет.\n'
    f'\nЖребий решил, что сначала ходит {", потом ".join(players)}.\n'
)

while rest_in_pot > 0:
    for player in players:
        print(f'Ходит {player}.')
        num = get_quantity(player, pot, rest_in_pot, max_take)
        rest_in_pot = rest_in_pot - num
        print(f'{player} берёт {num} конфет.')
        print(f'В банке осталось {rest_in_pot} конфет.\n')
        if rest_in_pot == 0:
            print(player, 'победил.')
            break
