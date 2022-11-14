import sys
from pathlib import Path

import model as m
import view as v


def get_file_name():
    return input_not_empty('Введите имя файла, например export: ',
                           'Файл не может быть пустым, введите имя файла.')


def input_not_empty(message, message_if_empty):
    while not (res := input(f'\n{message}')):
        print(message_if_empty)
    return res


def get_file_format():
    v.print_data(v.file_format_menu)
    file_format = input_not_empty('Ваш выбор: ', 'Выберите формат')
    match file_format:
        case '1':
            return 'csv'
        case '2':
            return 'json'
        case '3':
            return 'xml'
        case '4':
            return 'xlsx'
        case '0':
            sys.exit()


def get_user_data():
    # TODO словарь переводов названий полей
    # TODO валидация данных при вводе
    user_data = {field: input(f'Введите {field}: ')
                 for field in m.user_schema}
    count = 1
    while p := input('Введите телефон или оставьте поле пустым: '):
        user_data[f'phone_{str(count)}'] = p
        count += 1
    return user_data


def align_left_formatter(df, cols=None):
    if cols is None:
        cols = df.columns[df.dtypes == 'object']

    return {col: f'{{:<{df[col].str.len().max()}s}}'.format for col in cols}


def run():
    m.set_users(m.get_users('local_storage.json'))
    m.generate_random_users()
    v.clear_screen()

    while True:
        v.print_data(v.main_menu)
        match input('Ваш выбор: '):
            case '1':
                v.clear_screen()
                if m.local_data['users']:
                    df = m.get_dataframe()
                    v.print_data(df.to_string(index_names=False,
                                              header=False, na_rep='',  justify='left', formatters=align_left_formatter(df)))
                else:
                    v.print_data('Справочник пуст.')

            case '2':
                res = m.add_user(get_user_data())
                if res:
                    v.clear_screen()
                    if res[1]:
                        v.print_data(
                            f'Добавлен новый пользователь с id:{res[0]}')
                    else:
                        v.print_data(
                            f'Добавлен новый телефон к пользователю с id:{res[0]}')
            case '3':
                res = m.delete_user(
                    user_id := int(input('Введите id пользователя: ')))
                v.clear_screen()
                if res == 'success':
                    v.print_data(f'Пользователь c id {user_id} удалён.')
                else:
                    v.print_data(f'Нет пользователя c id: {user_id}')

            case '4':
                file_format = get_file_format()
                while not (Path((file_name := get_file_name()) + '.' + file_format)).is_file():
                    v.print_data(
                        'Такого файла нет. Введите правильное имя без расширения.')
                res = m.import_from_file(file_format, file_name)
                v.clear_screen()
                if res:
                    v.print_data(
                        f'Добавлено новых пользователей: {res[0]}, обновлено дубликатов: {res[1]}')
                else:
                    v.print_data('Ничего не импортировано')
            case '5':
                if m.local_data:
                    v.clear_screen()
                    res = m.export_to_file(get_file_format())
                    if res == 'success':
                        v.clear_screen()
                        v.print_data('Данные экспортированы.')
                else:
                    v.clear_screen()
                    v.print_data('Справочник пуст. Экспортировать нечего.')

            case '6':
                v.clear_screen()
                res = m.clear_users()
                if not res['users']:
                    v.print_data('Справочник очищен.')

            case '7':
                v.clear_screen()
                if m.generate_random_users():
                    v.print_data('Добавлено 10 случайных пользователей.')

            case '0':
                sys.exit()
