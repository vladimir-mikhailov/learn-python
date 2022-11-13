import os
import platform


main_menu = '''Выберите действие:
    1 - Показать справочник
    2 - Добавить пользователя
    3 - Удалить пользователя
    4 – Импортировать из файла
    5 – Экспортировать в файл
    6 – Очистить справочник
    7 - Добавить 10 случайных сгенерированных пользователей
    0 - Выход'''


file_format_menu = '''Выберите формат файла:
    1 - CSV
    2 - JSON
    3 - XML
    4 - Excel
    0 - Выход'''


def print_data(data):
    print(data, '\n')


def clear_screen():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        return os.system('clear')
    elif platform.system() == "Windows":
        return os.system('cls')
