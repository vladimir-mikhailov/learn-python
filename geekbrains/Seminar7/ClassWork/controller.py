# User interface, соединяет пользователя, фронт и бэк

import view
import model
import logger


def get_numbers():
    a = input('Введите число А: ')
    b = input('Введите число Б: ')
    return a, b


def run():
    while True:
        view.show_menu()
        answer = input('Ваш ответ:')

        match answer:
            case '1':
                model.init(*get_numbers())
                result = model.divide()
            case '2':
                model.init(*get_numbers())
                result = model.sum()
            case '3':
                model.init(*get_numbers())
                result = model.multiply()
            case '4':
                model.init(*get_numbers())
                result = model.sub()
            case '5':
                exit()

        view.show(result)
        logger.calculation_logger(result)
