import pandas as pd
import json
from faker import Faker

# TODO Переключить локальное хранилище на базу данных
local_data = {
    'users': [],
    'phones': []
}

user_schema = [
    'name',
    'last_name',
    'birth_date',
    'email',
    'job',
    'company'
]


def get_users(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


def set_users(data):
    global local_data
    local_data = data


def clear_users():
    global local_data
    local_data = {
        'users': [],
        'phones': []
    }
    return local_data


def get_dataframe():
    global local_data
    if local_data['users']:
        users_with_phones = local_data['users'].copy()
        for user in users_with_phones:
            count = 0
            for phone in local_data['phones']:
                if user['user_id'] == phone['user_id']:
                    count += 1
                    user[f'phone_{str(count)}'] = phone['phone_number']
        return pd.DataFrame(users_with_phones).set_index('user_id').fillna('')
    return pd.DataFrame([])


def import_from_file(file_format, file_name):
    file = file_name + '.' + file_format

    match file_format:
        case 'csv':
            df = pd.read_csv(file, na_values=[''], dtype=object)
        case 'json':
            df = pd.read_json(file, dtype=object)
        case 'xml':
            df = pd.read_xml(file, dtype=object)
        case 'xlsx':
            df = pd.read_excel(file, index_col=None, na_values=[''])
        case _:
            exit()
    duplicates = 0
    new_users = 0
    for user in df.to_dict(orient='records'):
        res = add_user(user)
        if res:
            if not res[1]:
                duplicates += 1
            else:
                new_users += 1
    return new_users, duplicates


def export_to_file(file_format):
    file = 'export' + '.' + file_format

    frame = get_dataframe()

    match file_format:
        case 'csv':
            frame.to_csv(file, index=False)
        case 'json':
            frame.to_json(file, orient='records', indent=4, force_ascii=False)
        case 'xml':
            frame.to_xml(file, index=False)
        case 'xlsx':
            frame.to_excel(file, index=False)
        case _:
            return 'error'

    return 'success'


def get_id():
    global local_data
    if not local_data['users']:
        return 0
    return max([user['user_id'] for user in local_data['users']]) + 1


def find_duplicate(user_data):
    global local_data
    for user in local_data['users']:
        user_no_id = user.copy()
        del user_no_id['user_id']
        if len(user_no_id) == len({k: user_no_id[k]
                                   for k in user_no_id if k in user_data and user_no_id[k] == user_data[k]}):
            return user['user_id']
    return -1


def add_user(user_data):
    global local_data

    for user in local_data['users']:
        duplicate_id = find_duplicate(user_data)
        if duplicate_id == -1:
            user_id = get_id()
            local_data['users'].append({
                'user_id': user_id,
                'name': user_data['name'],
                'last_name': user_data['last_name'],
                'birth_date': user_data['birth_date'],
                'email': user_data['email'],
                'job': user_data['job'],
                'company': user_data['company']
            })

            for phone in [user_data[key] for key in user_data.keys() if 'phone' in key]:
                local_data['phones'].append({
                    'user_id': user_id,
                    'phone_number': phone
                })

            return user_id, True

        else:
            user_id = duplicate_id
            for phone in [user_data[key] for key in user_data.keys() if 'phone' in key]:
                if phone not in [p['phone_number'] for p in local_data['phones'] if p['user_id'] == user_id]:
                    local_data['phones'].append({
                        'user_id': user_id,
                        'phone_number': phone
                    })
        return user_id, False
    return ''


def generate_random_users():
    global local_data
    fake = Faker(locale="ru_RU")

    for i in range(10):
        add_user({
            'name': fake.first_name_male(),
            'last_name': fake.last_name_male(),
            'birth_date': fake.date(),
            'email': fake.company_email(),
            'job': fake.job(),
            'company': fake.large_company(),
            'phone': fake.phone_number()
        })

    return 'ok'


def get_user(user_id):
    global local_data
    for user in local_data['users']:
        if user['user_id'] == user_id:
            return user
    return {}


def delete_user(user_id):
    global local_data
    for user in local_data['users']:
        if user['user_id'] == user_id:
            for key in local_data.keys():
                local_data[key] = list(filter(
                    lambda i: i['user_id'] != user_id, local_data[key]))
            return 'success'
    return '404'
