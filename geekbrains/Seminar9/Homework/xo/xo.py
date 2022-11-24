from tkinter import *
import random


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['fg'] = 'black'
    global game_run
    game_run = True
    global moves_count
    moves_count = 0
    global new_game_btn
    new_game_btn['state'] = DISABLED
    new_game_btn['text'] = 'Игра началась. Удачи!'


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global moves_count
        moves_count += 1
        if moves_count >= 5:
            check_win('X')
        if game_run:
            computer_move()
            if moves_count >= 5:
                check_win('O')


def check_win(xo):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], xo)
        check_line(field[0][n], field[1][n], field[2][n], xo)
    check_line(field[0][0], field[1][1], field[2][2], xo)
    check_line(field[2][0], field[1][1], field[0][2], xo)
    if moves_count == 9:
        global game_run
        game_run = False
        global new_game_btn
        new_game_btn['state'] = NORMAL
        new_game_btn['text'] = f'Ничья. Сыграем ещё?'


def check_line(a1, a2, a3, xo):

    if a1['text'] == xo and a2['text'] == xo and a3['text'] == xo:
        a1['fg'] = a2['fg'] = a3['fg'] = 'green'
        global game_run
        game_run = False
        global new_game_btn
        new_game_btn['state'] = NORMAL
        winner = 'Крестик' if xo == 'X' else 'Нолик'
        new_game_btn['text'] = f'{winner} победил. Сыграем ещё?'


def can_win(a1, a2, a3, xo):
    res = False
    if a1['text'] == xo and a2['text'] == xo and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == xo and a2['text'] == ' ' and a3['text'] == xo:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == xo and a3['text'] == xo:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    global moves_count
    moves_count += 1
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


if __name__ == '__main__':
    root = Tk()
    root.title('Крестики - Нолики')
    game_run = True
    field = []
    moves_count = 0

    for row in range(3):
        line = []
        for col in range(3):
            button = Button(root, text=' ', width=4, height=2,
                            font=('Verdana', 20, 'bold'),
                            fg='black',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky=W)
            line.append(button)
        field.append(line)
    new_game_btn = Button(root, text='Игра началась. Удачи!',
                          command=new_game, state=DISABLED)
    new_game_btn.grid(row=3, column=0, columnspan=3, sticky='nsew')
    root.mainloop()
