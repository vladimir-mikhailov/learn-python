from datetime import datetime as dt


def calculation_logger(data):
    '''Creates log file with current time and calculated value'''
    time = dt.now().strftime('%H:%M:%S')
    with open('log.json', 'a') as file:
        file.write(f'\n{time}; calculation; {data}\n')